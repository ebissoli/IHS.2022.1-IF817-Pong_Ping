cmd_/home/CIN/egb2/git/ihs-project-layout/driver/char/Module.symvers := sed 's/\.ko$$/\.o/' /home/CIN/egb2/git/ihs-project-layout/driver/char/modules.order | scripts/mod/modpost -m -a  -o /home/CIN/egb2/git/ihs-project-layout/driver/char/Module.symvers -e -i Module.symvers   -T -
