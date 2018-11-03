from Inject import Inject
from AttackVectorSimulation import AttackVectorSimulation
from Workflow import Workflow
import argparse

# Sets up parser
parser = argparse.ArgumentParser()
parser.add_argument("attack_type", help="put attack vector type")
parser.add_argument("number_of_threats", help="put number of threats wanted", type=int)

args = parser.parse_args()

# Code to call correct methods in order
i = Inject()
i.read()
a = AttackVectorSimulation(i.get_obj(), args.attack_type, args.number_of_threats)
a.insert_threats()
w = Workflow()
temp = i.get_obj()
temp2 = w.create_workflow_emails()
for email in temp2:
    temp.append(email)
i.set_obj(temp)
i.write()
