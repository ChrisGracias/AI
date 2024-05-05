from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the structure of the Bayesian Network
model = BayesianNetwork([('Burglary', 'Alarm'), ('Earthquake', 'Alarm'), ('Alarm', 'Mary'), ('Alarm', 'John')])

# Define the conditional probability distributions (CPDs)
cpd_burglary = TabularCPD(variable='Burglary', variable_card=2, values=[[0.999], [0.001]])
cpd_earthquake = TabularCPD(variable='Earthquake', variable_card=2, values=[[0.998], [0.002]])
cpd_alarm = TabularCPD(variable='Alarm', variable_card=2, values=[[0.999, 0.71, 0.06, 0.05], [0.001, 0.29, 0.94, 0.95]],
                       evidence=['Burglary', 'Earthquake'], evidence_card=[2, 2])
cpd_mary = TabularCPD(variable='Mary', variable_card=2, values=[[0.95, 0.1], [0.05, 0.9]], evidence=['Alarm'], evidence_card=[2])
cpd_john = TabularCPD(variable='John', variable_card=2, values=[[0.9, 0.05], [0.1, 0.95]], evidence=['Alarm'], evidence_card=[2])

# Add CPDs to the model
model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_mary, cpd_john)

# Check if the model is valid
print("Model is valid:", model.check_model())

# Perform inference
inference = VariableElimination(model)

# Query for the probability of Burglary given Alarm and Mary heard the alarm
result = inference.query(variables=['Burglary'], evidence={'Alarm': 1, 'Mary': 1})
print("Probability of Burglary given Alarm and Mary heard the alarm:")
print(result)

# Query for the probability of Earthquake given John heard the alarm
result = inference.query(variables=['Earthquake'], evidence={'John': 1})
print("\nProbability of Earthquake given John heard the alarm:")
print(result)
