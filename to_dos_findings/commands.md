# Useful Commands

This file is dedicated to documenting useful commands for various tasks. Feel free to add any commands that you find helpful during your development process. By keeping a collection of commands in this file, you can easily refer back to them whenever needed.

Please format each command as a separate code block using triple backticks (```), and provide a brief description or usage notes for each command. This will make it easier for others to understand and utilize the commands effectively.

Happy coding!

# Renaming files removing .200K

for file in *.200K*.fastq.gz; do mv -- "$file" "${file//.200K/}"; done

# Snakemake Command
snakemake -c 10 --snakefile ../../workflow/Snakefile --configfile config.yml --notemp -p 