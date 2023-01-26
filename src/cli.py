import click
import os

from loguru import logger

from src.save_manager import SaveManager


SAVES_FOLDER = r'C:\Users\56kyl\AppData\LocalLow\Nolla_Games_Noita'
BACKUPS_FOLDER = r'C:\Users\56kyl\Desktop\noita backups'


@click.group()
def cli():
    pass


@cli.command()
@click.argument('backup_name')
@click.argument('save_name', required=False, default='save00')
@click.option('--force', '-f', is_flag=True, help='Overwrite existing files')
def load(backup_name, save_name, force):
    logger.info(f'Loading backup from {backup_name} to {save_name} with force={force}...')
    save_manager = SaveManager(
        saves_folder=SAVES_FOLDER,
        backups_folder=BACKUPS_FOLDER,
    )
    save_manager.load(backup_name=backup_name, save_name=save_name, overwrite=force)
    logger.info('...Done')


@cli.command()
@click.argument('backup_name')
@click.argument('save_name', required=False, default='save00')
@click.option('--force', '-f', is_flag=True, help='Overwrite existing files')
def backup(backup_name, save_name, force):
    logger.info(f'Backing up from {save_name} to {backup_name} with force={force}...')
    save_manager = SaveManager(
        saves_folder=SAVES_FOLDER,
        backups_folder=BACKUPS_FOLDER,
    )
    save_manager.backup(backup_name=backup_name, save_name=save_name, overwrite=force)
    logger.info('...Done')


@cli.command()
def quicksave():
    logger.info('Quicksaving...')
    save_manager = SaveManager(
        saves_folder=SAVES_FOLDER,
        backups_folder=BACKUPS_FOLDER,
    )
    save_manager.backup(backup_name='quicksave', save_name='save00', overwrite=True)
    logger.info('...Done')


@cli.command()
def quickload():
    logger.info('Quickloading...')
    save_manager = SaveManager(
        saves_folder=SAVES_FOLDER,
        backups_folder=BACKUPS_FOLDER,
    )
    save_manager.load(backup_name='quicksave', save_name='save00', overwrite=True)
    logger.info('...Done')


@cli.command()
def list():
    logger.info(r'Backups in {backups_folder}:')
    for backup_name in os.listdir(BACKUPS_FOLDER):
        logger.info(f'\t{backup_name}')

