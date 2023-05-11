# read a fasta file and convert it to a pandas dataframe with two columns: ID and sequence
def read_fasta(fasta_file):
    with open(fasta_file, 'r') as f:
        lines = f.readlines()
    seq = []
    ID = []
    for line in lines:
        if line.startswith('>'):
            ID.append(line.strip()[1:])
        else:
            seq.append(line.strip())
    df = pd.DataFrame({'ID': ID, 'seq': seq})
    return df

# save the design dataframe to a fasta file
def save_fasta(df, fasta_file):
    with open(fasta_file, 'w') as f:
        for i in range(df.shape[0]):
            f.write('>' + df.iloc[i, 0] + '\n')
            f.write(df.iloc[i, 1] + '\n')
    return None  

def check_assignment(design, asso):
    design['type'] = 'unassigned'
    design.loc[design['seq'].str[15:-15].isin(asso['seq']), 'type'] = 'assigned'
    return design    

def find_homopolymer(col):
    hp = []
    for i in range(col.shape[0]):
        seq = col.iloc[i]
        longestrun = 0
        lbase, llen = 'N', 0
        for base in seq:
            if base == lbase:
                llen += 1
            else:
                if llen > longestrun:
                    longestrun = llen
                llen = 1
                lbase = base
        hp.append(longestrun)    
    return hp