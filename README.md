# AV-synth
This repo will store all AV-Synth software materials


## Building Hydra (contained) w/ Nix package manager & Nix Shell

The install instructions that hydra has should work, but NPM & Nodejs tend to sprawl and get out of hand. I found using nix-shell to be a good solution for setup and running the system, then leaving it entirely once you're done.

First you will want to install nix (refer to nixos.com/download). Generally, this line should do the trick:
```
  sh <(curl -L https://nixos.org/nix/install) --daemon
```
Sick, now you can open a nix-shell with the preconfigured packages that we need for hydra, then follow their installation instructions. The former looks like:
```
nix-shell default.nix
cd hydra
```
The latter will look like:

>install dependencies:
>```
>yarn install
>```
>run server
>```
>yarn serve
>```
>go to https://localhost:8000 in the browser


