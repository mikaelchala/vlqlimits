# VLQ-limits

VLQ-limits is a simple Python script that indicates whether a set of heavy top-like quarks with arbitrary branching ratios into Zt, Ht, Wb, St (with S being a scalar real singlet decaying either into bottom quarks or into missing energy) or into some other elusive final state is excluded at the 95 % C.L. in light of the following analyses:

- [1505.04306](http://arxiv.org/abs/1505.04306)
- [ATLAS-CONF-2016-102](http://cds.cern.ch/record/2219436)
- [ATLAS-CONF-2016-104](http://cds.cern.ch/record/2220371)
- [ATLAS-CONF-2017-015](http://cds.cern.ch/record/2257730)
- [CMS-PAS-SUS-16-029](http://cds.cern.ch/record/2205176)

Two executable files are included:

- code_indp.py: returns 1 if the input is excluded by at least one analysis. It returns 0 otherwise.
- code_comb.py: returns 1 if the input is excluded by the combination of all analyses. It returns 0 otherwise. It requires [PyROOT](http://root.cern.ch/pyroot).

The input format is:

% comments

massHeavyTop  massS  BR(T->WB)  BR(T->HT) + BR(T->ST, S->BB)  BR(T->ZT)  BR(T->ST, S -> INV)

massHeavyTop must be above 600 GeV (take for granted that smaller masses are excluded, ;-)). massS should be in the range (100, 400) GeV.

Please, cite [arXiv:1705.0xxxx](http://arxiv.org/abs/1705.0xxxx) if you use this code.
