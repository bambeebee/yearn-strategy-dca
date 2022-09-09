from brownie import Strategy, accounts, config, network, project, web3
from eth_utils import is_checksum_address
from scripts.helpful_scripts import (
    get_account,
)
import click


def main():
    yearnvaults = project.load(config["dependencies"][0]) #load the base vaults project to access the original Vault contract
    Vault = yearnvaults.Vault
    Token = yearnvaults.Token
    vault = Vault.at("0xdA816459F1AB5631232FE5e97a05BBBb94970c95")
    token = Token.at("0x6b175474e89094c44da98b954eedeac495271d0f")
    gov = "ychad.eth"  # ENS for Yearn Governance Multisig

    strategy = Strategy.deploy(vault, {"from": accounts[0]})
