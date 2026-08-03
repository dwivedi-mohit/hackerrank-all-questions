# Ansible: Packages Management

## Metadata

- **ID:** 841052
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Linux, DevOps, Ansible
- **Skills:** Ansible (Basic)

## Summary

This DevOps question evaluates Ansible, package management, and Linux concepts, ideal for junior-level roles. The task requires completing an Ansible playbook to remove a package and install a new one using specific modules.

## Problem Statement

The task is to complete a file stub "/home/ubuntu/841052-ansible-packages-management/playbook.yml" with one or more steps that do the following:

	
- Removes and purges all the configuration files of the existing package "discover" using the Ansible "apt" module.
	
- Installs a new package "apt-fast" (ppa:apt-fast/stable) using the Ansible "apt" and "apt_repository" modules.

 

Note

	
- The completed solution will be evaluated in a new, clean environment. Be sure everything is in the "/home/ubuntu/841052-ansible-packages-management" folder.
	
- All the tasks should be done within a simple "sudo solve" execution invoked from the question directory.
	
- Ansible is already installed.
	
- You have sudo access.

 

Grading

	
- The execution result of "sudo solve" invoked from the question directory solves the task.
	
- The package "discover" and all the configuration files do not exist.
	
- The package "apt-fast" exists.
	
- The Ansible module "apt" is used.
	
- The Ansible module "apt_repository" is used.

## Preview

The task is to complete a file stub "/home/ubuntu/841052-ansible-packages-manage
