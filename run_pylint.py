# Run this file to obtain your PEP 8 compliance score.

from pylint.lint import Run as run_pylint

print("### slimebox.py ###")
pylint_results = run_pylint(['Admin.py', '--good-names=i,j,k,x,y,z,ex,Run,_,r,g,b'], exit = False)
pylint_score = min(pylint_results.linter.stats.global_note, 9)

print(pylint_score)
