# CPU Scheduling

[![License: MIT](https://img.shields.io/github/license/ILoveBacteria/cpu-scheduling)](https://github.com/ILoveBacteria/cpu-scheduling/blob/master/LICENSE)
[![Issues](https://img.shields.io/github/issues/ILoveBacteria/cpu-scheduling)](https://github.com/ILoveBacteria/cpu-scheduling/issues)
[![Forks](https://img.shields.io/github/forks/ILoveBacteria/cpu-scheduling)](https://github.com/ILoveBacteria/cpu-scheduling/network/members)
[![Stars](https://img.shields.io/github/stars/ILoveBacteria/cpu-scheduling)]()
[![Watchers](https://img.shields.io/github/watchers/ILoveBacteria/cpu-scheduling)]()
[![Last commit](https://img.shields.io/github/last-commit/ILoveBacteria/cpu-scheduling)](https://github.com/ILoveBacteria/cpu-scheduling/commits/master)
[![Workflow](https://img.shields.io/github/actions/workflow/status/ILoveBacteria/cpu-scheduling/test.yml?label=test)](https://img.shields.io/github/actions/workflow/status/ILoveBacteria/cpu-scheduling/test.yml?label=test)
[![Workflow](https://img.shields.io/github/pipenv/locked/python-version/ILoveBacteria/cpu-scheduling)](https://img.shields.io/github/pipenv/locked/python-version/ILoveBacteria/cpu-scheduling)


## Description

This repository contains an implementation of three different CPU scheduling algorithms: **FIFS**, **Round Robin**, 
and **EDF**. These algorithms are commonly used in operating systems to manage the allocation of CPU time to 
different processes. 

- FIFS (First In First Served) is a simple scheduling algorithm that assigns CPU time to processes in the order they 
arrive. The first process that arrives is given priority over all subsequent processes until it completes or is blocked.

- Round Robin is another scheduling algorithm that assigns a fixed time slice to each process in turn. Once a process 
has used up its time slice, it is moved to the back of the queue and the next process is given a turn.

- EDF (Earliest Deadline First) is a real-time scheduling algorithm that prioritizes processes based on their deadlines. 
The process with the earliest deadline is given priority over all other processes until it completes or misses its deadline.

