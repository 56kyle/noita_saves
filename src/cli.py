import os

import click

from src.save import SaveManager


@click.group()
def cli():
    pass


@cli.command()
@click.argument('backup_name')
@click.argument('save_name', required=False, default='save00')
@click.option('--force', '-f', is_flag=True, help='Overwrite existing files')
def load(backup_name, save_name, force):
    print(f'Loading backup from {backup_name} to {save_name} with force={force}...')
    save_manager = SaveManager(
        saves_folder=r'C:\Users\56kyl\AppData\LocalLow\Nolla_Games_Noita',
        backups_folder=r'C:\Users\56kyl\Desktop\noita backups',
    )
    save_manager.load(backup_name=backup_name, save_name=save_name, overwrite=force)
    print('...Done')


@cli.command()
@click.argument('backup_name')
@click.argument('save_name', required=False, default='save00')
@click.option('--force', '-f', is_flag=True, help='Overwrite existing files')
def backup(backup_name, save_name, force):
    print(f'Backing up from {save_name} to {backup_name} with force={force}...')
    save_manager = SaveManager(
        saves_folder=r'C:\Users\56kyl\AppData\LocalLow\Nolla_Games_Noita',
        backups_folder=r'C:\Users\56kyl\Desktop\noita backups',
    )
    save_manager.backup(backup_name=backup_name, save_name=save_name, overwrite=force)
    print('...Done')


@cli.command()
def list():
    backups_folder = r'C:\Users\56kyl\Desktop\noita backups'
    print(r'Backups in {backups_folder}:')
    for backup_name in os.listdir(backups_folder):
        print(f'\t{backup_name}')

