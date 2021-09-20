from latexqol.conversion import copy_table
import numpy as np


head = ["head1", "head2", "head3", "head4"]
col1 = np.arange(0, 20, 1)
col2 = np.arange(20, 40, 1)
col3 = np.arange(40, 60, 1)
col4 = np.arange(60, 80, 1)

copy_table(head, col1, col2, col3, col4)
