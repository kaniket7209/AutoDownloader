from tabula import read_pdf
# import tabula
# df = tabula.read_pdf("Files/pdf{}.pdf".format(5), output_format='json', pages='all')[0]
# # convert PDF into CSV
# # tabula.convert_into("Files/pdf{}.pdf".format(i), "data.csv", output_format="csv", pages='all')
# print(df)
import pdftotree

pdftotree.parse("Files/pdf{}.pdf".format(i), html_path=None, model_type=None, model_path=None, favor_figures=True, visualize=False):