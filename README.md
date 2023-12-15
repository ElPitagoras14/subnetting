# IP Segmentation Algorithm

## Table of Content

1. [Description](#description)
2. [Use](#use)
   - [FLSM by network](#flsm-by-minimal-networks)
   - [FLSM by host](#flsm-by-minimal-hosts)
   - [VLSM sorted host](#vlsm-by-sorted-hosts)
   - [VLSM host](#vlsm-by-hosts)
   - [Print subnets](#print-subnets)
   - [Save subnets to a file](#save-subnets-to-a-file)
   - [Create subnet tree](#create-subnet-tree)
   - [Generate tree string](#generate-tree-string)
   - [Save tree](#save-tree)
3. [Terms and Equations](#terms-and-equations)
4. [FLSM](#flsm-fixed-length-subnet-mask)
   - [Algorithm](#algorithm)
   - [Example](#example)
5. [VLSM](#vlsm-variable-length-subnet-mask)
   - [Algorithm](#algorithm-1)
   - [Example](#example-1)

## Use

All the subnetting functions return the following structure:

```json
{
    "subnet_info": "<vlsm info> | <flsm info>",
    "networks": [
        {
            "name": "<net name>",
            "subnet": "<ip>",
            "mask": "<mask>",
            "first_ip": "<first ip>",
            "last_ip": "<last valid ip>",
            "broadcast": "<last ip>",
        },
        {

        },
        {
            "name": "<net name>",
            "subnet": "<ip>",
            "mask": "<mask>",
            "first_ip": "<first ip>",
            "last_ip": "<last valid ip>",
            "broadcast": "<last ip>",
        }
    ]
}

{
    "vlsm_info": {
        "initial_ip": "<ip>",
        "initial_mask": "<mask>",
        "initial_host_per_network": "<host list>",
        "host_per_network": "<final host list>",
    },
}

{
    "flsm_info": {
        "initial_ip": "<ip>",
        "initial_mask": "<mask>",
        "n": "<n>",
        "m": "<m>",
        "number_of_networks": "<number of networks>",
        "number_of_hosts": "<number of host per network>",
    },
}
```

### FLSM by minimal networks

It performs subnetting with the FLSM technique passing as arguments the initial ip, the network mask and the number of minimum networks it needs.

```python
def networks_FLSM(ip: str, mask: int, min_networks: int):
    # method
```

### FLSM by minimal hosts

It performs subnetting with the FLSM technique passing as arguments the initial ip, the network mask and the number of minimum hosts it needs.

```python
def host_FLSM(ip: str, mask: int, min_host: int):
    # method
```

### VLSM by sorted hosts

It performs subnetting with the VLSM technique passing as arguments the initial ip, the network mask and a list of the number of hosts per network needed.

Additionally, this function sorts the list before subnetting.

```python
def ordered_host_VLSM(ip: str, mask: int, host_list: list[int]):
    # method
```

### VLSM by hosts

It performs subnetting with the VLSM technique passing as arguments the initial ip, the network mask and a list of the number of hosts per network needed.

```python
def host_VLSM(ip: str, mask: int, host_list: list[int]):
    # method
```

### Print subnets

This function displays a console table with the subnetting performed by any of the previous functions.

Receives the subnetting dictionary as arguments and optionally a string list parallel to the number of items in the dictionary to display each network with a custom name otherwise it prints **Net i**.

```python
def print_subnets(networks: list, names_list: list = None):
    # method
```

### Save subnets to a file

This function saves a table with the subnetting performed by any of the previous functions in a file.

Receives the subnetting dictionary as arguments, optionally a list of strings parallel to the number of items in the dictionary to save each network with a custom name, otherwise it prints **Net i** and optionally a directory to save it.

```python
def write_subnets(networks: list, names_list: list = None, path: str = "./networks.txt"):
    # method
```

### Create Subnet Tree

This function creates a binary tree structure using nodes. It represents the subnet tree.

Receives the initial ip, initial mask and the list of networks. All of this information can be obtained with the subnet functions.

```python
def create_tree(subnet: dict):
    # method
```

### Generate Tree String

This functions generates a console printable string to see the tree structure.

Receives the root of the tree, it can be obtained with `create_tree` function.

```python
def tree_to_str(node: SubnettingNode, prev: Trunk = None, isRight: bool = False):
    # method

# Example
subnet_info = networks_FLSM("192.168.0.0", 24, 4)
tree = create_tree(subnet_info)
tree_str = tree_to_str(tree)
print(tree_str)
```

### Save Tree

This function saves the tree to a txt file.

Receives the tree string and saves it to the passed path.

```python
def save_tree(tree_str: str, path: str = "./tree.txt"):
    # method
```

## Terms and Equations

- Number of subnet bits = $n$
- Number of host bits = $m$
- $32 = PrevMask + n + m$
- Number of subnets = $2^n$
- Block size = $2^m$
- Number of usable hosts = $2^n-2$
- $NewMask = LastMask+n$

## FLSM (Fixed Length Subnet Mask)

The division of the network is required to be in fixed blocks, that is, the same number of hosts in each subnet.

### Algorithm

1. The values of $n$ and $m$ are determined with the previous equations.
2. The new mask is determined by $LastMask+n$
3. Calculate how the IP will grow if the number of hosts per subnet is greater than $256$ by dividing $2^m/256$. Otherwise, only the host number is increased to the new subnet with the new mask.

### Example

**14 hosts per subnet** are required for address **199.6.14.0/25.**

$$
32=n+m+25\rightarrow n+m=7;
$$

$$
2^m-2\ge 14\rightarrow m=4\rightarrow n=3
$$

$$
Mask=25+n\rightarrow n=28
$$

| IP           | Mask | Subnet       | Broadcast    |
| ------------ | ---- | ------------ | ------------ |
| 199.6.14.0   | 28   | 199.6.14.0   | 199.6.14.15  |
| 199.6.14.16  | 28   | 199.6.14.16  | 199.6.14.31  |
| 199.6.14.32  | 28   | 199.6.14.32  | 199.6.14.47  |
| 199.6.14.48  | 28   | 199.6.14.48  | 199.6.14.63  |
| ...          | 28   | ...          | ...          |
| 199.6.14.112 | 28   | 199.6.14.112 | 199.6.14.127 |

## VLSM (Variable-Length Subnet Mask)

The division of the network is required to be in blocks of variable size, that is, there can be different numbers of hosts in each subnet.

The VLSM process is similar to performing FLSM for each new subnet.

### Algorithm

1. Order the subnets from highest to lowest depending on the number of hosts in each one.
2. For the first subnet, determine $n$ and $m$ from the above equations.
3. Get the new netmask by adding the previous netmask with $n$.
4. Take note of the IP address of the following subnet.
5. Repeat steps 2 to 4 for the following subnets

### Example

**Network of 100, 50, 25 and 25 hosts is required.** Starting at **IP address 200.10.100.0/24.**

| IP             | Host | n   | m   | Mask | Subnet         | Broadcast      |
| -------------- | ---- | --- | --- | ---- | -------------- | -------------- |
| 200.10.100.0   | 100  | 1   | 7   | 25   | 2000.10.100.0  | 200.10.100.127 |
| 200.10.100.128 | 50   | 1   | 6   | 26   | 200.10.100.128 | 200.10.100.191 |
| 200.10.100.192 | 25   | 1   | 5   | 27   | 200.10.100.192 | 200.10.100.223 |
| 200.10.100.224 | 25   | 0   | 5   | 27   | 200.10.100.224 | 200.10.100.255 |
