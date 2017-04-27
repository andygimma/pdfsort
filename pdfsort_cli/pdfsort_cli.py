import click
import time
import PyPDF2
import os
import sys

from pdf_sort import PDFSort
scriptpath = "../pdfsort/pdfsort.py"
sys.path.append(os.path.abspath(scriptpath))
from pdfsort.pdfsort import PDFSort
#
# @click.group(invoke_without_command=False)
# @click.pass_context
# def cli(ctx):
#     print "hello"
#     pass

@click.group(invoke_without_command=False)
@click.pass_context
def cli(ctx):
    pass

@cli.command()
@click.argument('input_pdf')
@click.argument('output_pdf')
@click.argument('pages_list')
def generate(input_pdf, output_pdf, pages_list):
    p = PDFSort(input_pdf)
    p.generate_pdf(output_pdf, pages_list)
    p.write_generated_pdfs()
    p.close()

@cli.command()
@click.argument('input_pdf')
@click.argument('output_pdf')
def flip(input_pdf, output_pdf):
    p = PDFSort(input_pdf)
    p.flip()
    p.write_temp_pdf(output_pdf)
    p.close()

@cli.command()
@click.argument('input_pdf')
@click.argument('output_pdf')
@click.argument('pages_list')
@click.argument('degrees')
def rotate_pages(input_pdf, output_pdf, pages_list, degrees):
    p = PDFSort(input_pdf)
    p.rotate_page_numbers(pages_list, int(degrees))
    p.write_temp_pdf(output_pdf)
    p.close()

@cli.command()
@click.argument('input_pdf')
@click.argument('increment')
def split(input_pdf, increment):
    p = PDFSort(input_pdf)
    p.split_existing_pdf(input_pdf, int(increment))
    p.close()

if __name__ == '__main__':
    cli()
## TODO Write to a directory
## TODO click output
## TODO Tkinter
## os.chdir(path)
# from os import walk
#
# f = []
# d = []
# for (dirpath, dirnames, filenames) in walk('kedsort'):
#     f.extend(filenames)
#     d.extend(dirnames)
#     break
