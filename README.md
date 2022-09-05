# IP Segmentation Algorithm

## Table of Content

1. [Description](#description)
2. [Class Use](#class-use)
   - [FLSM by network](#flsm-by-minimal-networks)
   - [FLSM by host](#flsm-by-minimal-hosts)
   - [VLSM sorted host](#vlsm-by-sorted-hosts)
   - [VLSM host](#vlsm-by-hosts)
   - [Show dictionary](#print-by-console)
   - [Save dictionary to a file](#save-dictionary-to-a-file)
   - [Create tree](#create-tree)
   - [Print tree](#print-tree)
   - [Save tree](#save-tree)
3. [Classless Use](#classless-use)
   - [FLSM by network](#flsm-by-minimal-networks-1)
   - [FLSM by host](#flsm-by-minimal-hosts-1)
   - [VLSM sorted host](#vlsm-by-sorted-hosts-1)
   - [VLSM host](#vlsm-by-hosts-1)
   - [Show dictionary](#print-by-console-1)
   - [Save dictionary to a file](#save-dictionary-to-a-file-1)
4. [Terms and Equations](#terms-and-equations)
5. [FLSM](#flsm-fixed-length-subnet-mask)
   - [Algorithm](#algorithm)
   - [Example](#example)
6. [VLSM](#vlsm-variable-length-subnet-mask)
   - [Algorithm](#algorithm-1)
   - [Example](#example-1)

## Description

Code written in python where the algorithm for IP segmentation with FLSM and VLSM techniques is used.

## Class Use

Making use of the functions is done via the `Subnetting` class in the API.py file, there are 4 options for subnetting and 2 functions for presenting the subnets. Additionally there is some example code in `./example2.py`.

All the functions save a dictionary in the class instance where the key is the network number and the value is a list with the subnet ip, new mask and broadcast ip.

### Create Instance

To create an instance of the class is a trivial process. From there, you have to set the values using `set_values` where you must pass the ip and the initial mask.

Once these steps have been carried out, the functions for subnetting can be used by passing the required parameters.

```python
sbnt = Subnetting()
sbnt.set_values("192.168.0.0", 22)
```

### FLSM by minimal networks

It performs subnetting with the FLSM technique passing as argument the number of minimum networks it needs.

```python
sbnt.network_FLSM(4) #Save the result in sbnt.dic
```

### FLSM by minimal hosts

It performs subnetting with the FLSM technique passing as argument the number of minimum hosts per network it needs.

```python
sbnt.host_FLSM(200) #Save the result in sbnt.dic
```

### VLSM by sorted hosts

It performs subnetting with the VLSM technique passing as argument a list of the number of hosts per network needed.

Additionally, this function sorts the list before subnetting.

```python
sbnt.host_sort_VLSM([50, 25, 100, 25]) #Save the result in sbnt.dic
```

### VLSM by host

It performs subnetting with the VLSM technique passing as argument a list of the number of hosts per network needed.

It is necessary that the addressing tree has been made so that the list has consistency with the hosts and networks.

```python
sbnt.host_VLSM([50, 25, 100, 25]) #Save the result in sbnt.dic
```

### Print dictionary

This function displays a console table with the subnetting performed by any of the previous functions.

Receives as optional arguments a string list parallel to the number of items in the dictionary to display each network with a custom name otherwise it prints **Net i**.

```python
sbnt.print_subnets() #Print dictionary
sbnt.print_subnets(nombres) #Print dictionary
```

### Save dictionary to a file

This function saves a table with the subnetting performed by any of the previous functions in a file.

Receives as optional arguments a list of strings parallel to the number of items in the dictionary to save each network with a custom name, otherwise it prints **Net i** and optionally a directory to save it.

```python
sbnt.write_subnets() #Save to networks.txt listed as Net i
sbnt.write_subnets(nombres) #Save in networks.txt listed as the names of the list
sbnt.write_subnets(nombres, "resultados.txt") #Save in results.txt listed as the names of the list
```

### Create tree

It is possible to create a tree in a simple way once you have the subnetting dictionary made with any of the 4 previous methods.

```python
sbnt.create_tree() #Create and saves tree structure in sbnt.tree and str form in sbnt.tree_str
```

### Print tree

To print the tree just call the method. No arguments needed.

```python
sbnt.print_tree()
```

```plaintext
#Example Ouput
        .——— 24-Net 4
    .——— 23
   |    `——— 24-Net 3
——— 22
   |    .——— 24-Net 2
    `——— 23
        `——— 24-Net 1
```

### Save tree

To save just call the method with the optional path argument.

```python
sbnt.save_tree()
```

## Classless Use

The previously shown functions can be applied without the class, they are also found in the `subnetting.py` file and can be used without problems, but we recommend using the `Subnetting` class.

All the functions return a dictionary where the key is the network number and the value is a list with the subnet ip, new mask and broadcast ip. Additionally there is some example code in `./example1.py`.

### FLSM by minimal networks

It performs subnetting with the FLSM technique passing as arguments the initial ip, the network mask and the number of minimum networks it needs.

```python
def red_FLSM(ip: str, mascara: int, redes_minima: int):
    #method
```

### FLSM by minimal hosts

It performs subnetting with the FLSM technique passing as arguments the initial ip, the network mask and the number of minimum hosts it needs.

```python
def host_FLSM(ip: str, mascara: int, host_minimo: int):
    #method
```

### VLSM by sorted hosts

It performs subnetting with the VLSM technique passing as arguments the initial ip, the network mask and a list of the number of hosts per network needed.

Additionally, this function sorts the list before subnetting.

```python
def host_ord_VLSM(ip: str, mascara: int, lista: list):
    #method
```

### VLSM by hosts

It performs subnetting with the VLSM technique passing as arguments the initial ip, the network mask and a list of the number of hosts per network needed.

```python
def host_VLSM(ip: str, mascara: int, lista: list):
    #method
```

### Print dictionary

This function displays a console table with the subnetting performed by any of the previous functions.

Receives the subnetting dictionary as arguments and optionally a string list parallel to the number of items in the dictionary to display each network with a custom name otherwise it prints **Net i**.

```python
def print_subnets(dic_redes: dict, nombres: list = None):
    #method
```

### Save dictionary to a file

This function saves a table with the subnetting performed by any of the previous functions in a file.

Receives the subnetting dictionary as arguments, optionally a list of strings parallel to the number of items in the dictionary to save each network with a custom name, otherwise it prints **Net i** and optionally a directory to save it.

```python
def write_subnets(dic_redes: dict, nombres: list = None, path: str = "./redes.txt"):
    #method
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
