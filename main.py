import argparse
import os
parser = argparse.ArgumentParser(description='sort similar type of files into subdirectories of the input directory')

parser.add_argument('input_directory',type=str,help='inputting the directory adress')

args = parser.parse_args()
direc = args.input_directory
path_text=direc+'\\text'
path_pics=direc+'\\pics'
path_aud=direc+'\\aud'
path_vid=direc+'\\vid'
path_prgm=direc+'\\prgm'
path_img=direc+'\\img'
path_comparch=direc+'\\comparch'
path_webpg=direc+'\\webpg'
path_unknown=direc+'\\unknown'
list_dir = []






for dir_path, dir_name, file_name in os.walk(direc):
    list_dir.extend(dir_name)
    for name in file_name:
        if name.endswith((".doc", ".docx", ".rtf", ".pdf", ".wpd",".txt",".csv",".wps",".msg")):
                if not os.path.isdir(path_text):
                    os.mkdir(path_text)
                os.replace(dir_path+"\\"+"\\"+name, path_text+"\\"+"\\"+name)

        elif name.endswith((".JPEG", ".PNG", ".GIF", ".HEIF",".jpg",".png",".webp",".tif",".bmp",".eps")):
                if not os.path.isdir(path_pics):
                    os.mkdir(path_pics)
                os.replace(dir_path+"\\"+name, path_pics+"\\"+name)
        
        elif name.endswith((".aac", ".mp3", ".wav",".wma",".snd",".ra",".au")):
                if not os.path.isdir(path_aud):
                    os.mkdir(path_aud)
                os.replace(dir_path+"\\"+name, path_aud+"\\"+name)

        elif name.endswith((".amv", ".mpeg", ".flv", ".avi",".3gp",".mp4",".mpg",".mov",".wmv")):
                if not os.path.isdir(path_vid):
                    os.mkdir(path_vid)
                os.replace(dir_path+"\\"+name, path_vid+"\\"+name)
        elif name.endswith((".c", ".java", ".py", ".js",".cpp",".cs",".ts",".swelift",".dta",".pl",".sh",".bat",".com",".exe")):
                if not os.path.isdir(path_prgm):
                    os.mkdir(path_prgm)
                os.replace(dir_path+"\\"+name, path_prgm+"\\"+name)

        elif name.endswith((".iso", ".rar", ".tar", ".7z",".zip",".hqx",".arj",".tar",".arc",".sit",".gz",".z")):
                if not os.path.isdir(path_comparch):
                    os.mkdir(path_comparch)
                os.replace(dir_path+"\\"+name, path_comparch+"\\"+name)

        elif name.endswith((".html", ".asp", ".css", ".xps",".xhtml",".htm",".aspx",".rss")):
                if not os.path.isdir(path_webpg):
                    os.mkdir(path_webpg)
                os.replace(dir_path+"\\"+name, path_webpg+"\\"+name)
                
       
            
        else:
            if '.' in name:
                s=direc +"\\"
                for i in range(len(name)-1,0,-1):
                    if name[i]=='.':
                        for j in range(i+1,len(name)):
                                    s+=name[j]
                        break

                if not os.path.isdir(s):
                    os.mkdir(s)
                os.replace(dir_path+"\\"+name, s+"\\"+name)
            else:
                if not os.path.isdir(path_vid):
                    os.mkdir(path_unknown)
                os.replace(dir_path+"\\"+name,path_unknown+"\\"+name)


for dir_path, dir_name, file_name in os.walk(direc, topdown=False):
    for dirname in dir_name:
        if dirname in list_dir:
            try:
                os.rmdir()
            except:
                pass
            