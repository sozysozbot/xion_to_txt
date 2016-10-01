import docx2txt
import codecs
import os

indir = "D:\\xion_to_txt\\xion_to_txt-master\\docs\\"
outdir = "D:\\xion_to_txt\\txts_docx2txt\\"

inputs = os.listdir(indir)

for i in inputs:
    f = codecs.open(outdir+i+".txt", "w", "utf-8")
    f.write(docx2txt.process(indir+i))
    f.close()


