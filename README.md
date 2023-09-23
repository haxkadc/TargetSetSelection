# TargetSetSelection
University Project: Minimum Target Set

**Instance:**
A network **G = (V,E)** with thresholds t : V → N. 

**Problem:** 
Find a target set S ⊆ V of minimum size for **G**.

<pre> Find smallest S such that Influenced[S,∞]= V </pre>

##
## Datasets

The datasets used for the following project are “political.csv” and “email-Eu-core.csv”.

The first contains network data for books on U.S. policy that were published around the time of the 2004 presidential election and co-purchased by the buyers themselves. Data originally compiled and analyzed by Valdis Krebs. The dataset contains 105 nodes and 441 unweighted and indirect arcs and was taken from the following GitHub repository 
https://github.com/melaniewalsh/sample-social-network-datasets/tree/master/sample-datasets/political-books.

Email-Eu-core.csv contains data from a network generated using email data from a large European research institute. Emails only represent communication between members of the institution, and the dataset does not contain incoming messages or outgoing messages to the rest of the world.

In addition, the dataset also contains memberships to the "ground-truth" community of nodes. Each individual belongs to exactly one of the 42 departments of the research institute. This network represents the “core” of the email-EuAll network, which also contains links between members of the institution and people outside the institution.

The dataset contains 1005 nodes and 25571 arcs and was taken from the following repository https://snap.stanford.edu/data/email-Eu-core.html.


##
## Algorithm
The algorithm used in the project is Target Set Selection (TSS), below is the TSS pseudocode.


    

<img width="200" alt="Schermata 2023-09-22 alle 15 45 47" src="https://github.com/haxkadc/TargetSetSelection/assets/134702013/9f28d44e-c9fe-4b21-930c-38428c0cf1be">  
<img width="572" alt="Schermata 2023-09-22 alle 16 14 40" src="https://github.com/haxkadc/TargetSetSelection/assets/134702013/d8039fb5-0198-4e86-9b55-a7bc020c4905">




<img width="800" alt="Schermata 2023-09-22 alle 16 03 47" src="https://github.com/haxkadc/TargetSetSelection/assets/134702013/bcef7eae-447c-4bdf-93ee-04a1eae35964">

##
## Results

In Output folder there are the files create from political.csv dataset with graph representation and list of nodes/edges.

**Example**
<p align="center">

<img width="400" src="https://github.com/haxkadc/TargetSetSelection/blob/main/Output/output.png">

</p>

In Plot folder there are different type of plot created with Algorithms TSS Probabilistic and Tss Deterministic and different nodes threshold.

**Example**

<p align="center">
<img src="https://github.com/haxkadc/TargetSetSelection/blob/main/Plot/Plot-Th-crescente-Pr-crescente_Political_csv.png">

</p>
