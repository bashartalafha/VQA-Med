import re
class Utility(object):
    @staticmethod
    def clean(line):
        line = line.lower()
        line = line.replace('?', ' ?')
        line = re.sub(' +',' ', line)
        return line.strip()     
    
    @staticmethod
    def read_dataset(dataset):
        path="dataset/VQAMed2018"+dataset+"/VQAMed2018"+dataset+"-QA.csv"
        df =pd.read_csv(path, sep='\t', header=None, quoting=csv.QUOTE_NONE)
        if "Test" in dataset:
            df = df.rename(columns={0: 'id', 1: 'image_name', 2:"question"})
        else:
            df = df.rename(columns={0: 'id', 1: 'image_name', 2:"question", 3:"answer"})
        print(dataset+" data size=",len(df))
        images = []
        for i in df["image_name"]:

            fname = "dataset/VQAMed2018"+dataset+"/VQAMed2018"+dataset+"-images/"+i+".jpg"
            images.append(fname)
        if "Test" in dataset:
            return images, df["question"]
        else:
            return images, df["question"], df["answer"]

