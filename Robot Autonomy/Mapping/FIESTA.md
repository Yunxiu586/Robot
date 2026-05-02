# FIESTA

[toc]

### Overview

For a fully autonomous Micro Aerial Vehicle (**MAV**), the perception-planning-control pipeline takes environmental measurements as input and generates control commands.

**F**ast **I**ncremental **E**uclidean Di**STA**nce Fields (**FIESTA**) is a lightweight and flexible mapping framework for building ESDF map incrementally.

+ Firstly, we get depth measurements and pose measurements.
+ **Raycasting** is used to integrate measurements into the occupancy grid map in FIESTA. In this process, voxels whose occupancy status changes are added to `insertQueue` and `deleteQueue` respectively.
+ After that, merge these 2 queues into a queue named `updateQueue` by **ESDF Update Initialization** and update all the voxels that ESDF may change using **ESDF Updating Algorithm** based on BFS.

### Data Structures

##### Occupancy Grid Map & Voxel Information Structure

FIESTA uses an **Occupancy Grid Map** to integrate occupancy information from depth measurements. 

The information of each voxel is stored in a **Voxel Information Structure**, abbreviated as **VIS**. A VIS contains both occupancy information and ESDF-related information. The main members and methods are in the table below.

| Name                              | Meaning                                             | Abbreviation           |
| --------------------------------- | --------------------------------------------------- | ---------------------- |
| position                          | voxel coordinate                                    | `pos`                  |
| occupancy                         | probability of occupancy                            | `occ`                  |
| ESDF                              | **Euclidean distance to the closest obstacle**      | `dis`                  |
| Closest Obstacle Voxel Coordinate | **voxel coordinate of the closest obstacle**        | `coc`                  |
| observed                          | whether this voxel is ever observed                 | `obs`                  |
| prev, next, head                  | pointers used in DLLs                               | `prev`, `next`, `head` |
| Doubly Linked List method         | **all voxels whose closest obstacle is this voxel** | `dll`                  |
| Neighborhoods method              | all observed neighbors of this voxel                | `nbrs`                 |

##### Indexing Data Structure

The **Indexing Data Structure** maps a voxel coordinate to the corresponding pointer of VIS. 

If the bounding box is known and memory is sufficient, a voxel can be queried by computing its array index directly. If the bounding box is unknown or memory is limited, Hash Table stores only observed voxels but requires higher lookup cost. FIESTA therefore uses a hash table indexes blocks, while each block stores `VIS` pointers in an array, reducing hash-table size while keeping dynamic extensibility.

##### Doubly Linked Lists

The **Doubly Linked Lists**, abbreviated as **DLLs**, are used especially for efficient ESDF updating when an occupied voxel becomes free. For a voxel `vox`, the method `vox.dll` represents all voxels whose closest obstacle is `vox`.
$$
\texttt{x.coc} = \texttt{vox.pos}
$$
At the beginning, the closest obstacles of all voxels are initialized to **Ideal Point**, namely **Point at Infinity**, denoted by `IP`.

FIESTA uses `INSERTINTODLL` and `DELETEFROMDLL` to maintain these DLLs. With the Indexing Data Structure and DLL pointers, inserting or deleting a given node can be implemented in constant time.

### Algorithm

##### ESDF Updating Initialization Algorithm

**ESDF Updating Initialization** merges `insertQueue` and `deleteQueue` into `updateQueue`.

For voxels in `insertQueue`,  a voxel that becomes occupied is itself an obstacle. Therefore, its closest obstacle coordinate becomes its own position, and its ESDF distance becomes zero.

$$
\texttt{cur.coc} \leftarrow \texttt{cur.pos}
$$

$$
\texttt{cur.dis} \leftarrow 0
$$

For voxels in `deleteQueue`, when an occupied voxel `cur` becomes unoccupied, every voxel in `cur.dll` may lose its closest obstacle. FIESTA clears these voxels back to the observed-but-not-yet-updated state, 
$$
\texttt{vox.coc} \leftarrow \texttt{IP}
$$

$$
\texttt{vox.dis} \leftarrow \texttt{infinity}
$$

then tries to reassign their `coc` and `dis` using existing closest obstacles from their observed neighbors.
$$
\texttt{vox.dis} \leftarrow \texttt{DIST(nbr.coc, vox.pos)}
$$

$$
\texttt{vox.coc} \leftarrow \texttt{nbr.coc}
$$

```pseudocode
Procedure ESDFUpdatingInitialization(insertQueue, deleteQueue)

while not insertQueue.EMPTY() do
    cur <- insertQueue.FRONT()
    insertQueue.POP()

    DELETEFROMDLL(cur.coc, cur.pos)
    cur.coc <- cur.pos
    cur.dis <- 0
    INSERTINTODLL(cur.coc, cur.pos)

    updateQueue.PUSH(cur)
end while

while not deleteQueue.EMPTY() do
    cur <- deleteQueue.FRONT()
    deleteQueue.POP()

    for each vox in cur.dll do
        DELETEFROMDLL(vox.coc, vox.pos)
        vox.coc <- IP
        vox.dis <- infinity

        for each nbr in vox.nbrs do
            if nbr.coc still existing and DIST(nbr.coc, vox.pos) < vox.dis then
                vox.dis <- DIST(nbr.coc, vox.pos)
                vox.coc <- nbr.coc
            end if
        end for

        if vox.coc == IP then
            INSERTINTODLL(IP, vox.pos)
        else
            INSERTINTODLL(vox.coc, vox.pos)
            updateQueue.PUSH(vox)
        end if
    end for
end while
```

##### ESDF Updating Algorithm with Limited-Observation Patch  

The first `for` loop is the limited-observation patch. It makes `cur` check whether it can be updated from existing neighbors before it propagates information outward. 

The second `for` loop is the ESDF updating step. It uses `cur.coc` as the candidate closest obstacle for each `nbr`.
$$
\texttt{nbr.dis} \leftarrow \texttt{DIST}(\texttt{cur.coc}, \texttt{nbr.pos})
$$

$$
\texttt{nbr.coc} \leftarrow \texttt{cur.coc}
$$

```pseudocode
Procedure ESDFUpdatingAlgorithmWithLimitedObservationPatch(updateQueue)

while not updateQueue.EMPTY() do
    cur <- updateQueue.FRONT()
    updateQueue.POP()

    flag <- false

    for each nbr in cur.nbrs do
        if DIST(nbr.coc, cur.pos) < cur.dis then
            cur.dis <- DIST(nbr.coc, cur.pos)
            DELETEFROMDLL(cur.coc, cur.pos)
            cur.coc <- nbr.coc
            INSERTINTODLL(cur.coc, cur.pos)
            flag <- true
        end if
    end for

    if flag then
        updateQueue.PUSH(cur)
        continue
    end if

    for each nbr in cur.nbrs do
        if DIST(cur.coc, nbr.pos) < nbr.dis then
            nbr.dis <- DIST(cur.coc, nbr.pos)
            DELETEFROMDLL(nbr.coc, nbr.pos)
            nbr.coc <- cur.coc
            INSERTINTODLL(nbr.coc, nbr.pos)
            updateQueue.PUSH(nbr)
        end if
    end for
end while
```

### Theoretical Analysis

##### Optimality

FIESTA updates each voxel by checking the `coc` values of its `nbrs`, so the candidate obstacles come only from neighboring voxels instead of all obstacles in the map. 
$$
\texttt{cur.dis} \leftarrow \min_{\texttt{nbr} \in \texttt{cur.nbrs}} \texttt{{DIST}(nbr.coc, cur.pos)}
$$

with the corresponding closest obstacle coordinate updated as

$$
\texttt{cur.coc} \leftarrow \texttt{nbr}^{*}.\texttt{coc}
$$

where

$$
\texttt{nbr}^{*}
=
\arg\min_{\texttt{nbr} \in \texttt{cur.nbrs}}
\texttt{{DIST}(nbr.coc, cur.pos)}
$$

Therefore, the computed `dis` is always a **true Euclidean distance** to some obstacle, but it is not guaranteed to be the globally shortest one. If the real closest obstacle is not included in the neighbors’ `coc` set, FIESTA may produce a **near-optimal** rather than exact ESDF value. 

##### Time Complexity

For **ESDF Updating Initialization**, each voxel that is either in `insertQueue` or whose closest obstacle is in `deleteQueue` is handled only once. If an FIFO queue is used, the **time complexity** is
$$
\Theta(k)
$$

where $k$ is the number of all necessary voxels needed to be handled during initialization.

For **ESDF Updating Algorithm**, if a priority queue is used to perform the BFS procedure, every voxel is popped from `updateQueue` and handled only once to update its neighbors. The time complexity is

$$
\Theta(n \log n)
$$

where $n$ is the number of all voxels that need to be updated. The factor $\log n$ comes from the priority queue.

##### Space Complexity

Compared with a hash-table-based occupancy grid map, FIESTA introduces only constant-level memory overhead because each observed voxel stores one additional `VIS`, including `dis`, `coc`, `obs`, and DLL pointers. With `block_size = 1`, the `Indexing Data Structure` reaches

$$
\Theta(m)
$$

where $m$ is the number of all ever observed voxels.