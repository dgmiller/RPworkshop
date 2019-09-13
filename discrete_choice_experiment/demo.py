import utils

metadata = dict()
metadata['nresp'] = 5
metadata['ntask'] = 5
metadata['nalts'] = 3
metadata['nlvls'] = 10
metadata['ncovs'] = 1

design_dict = utils.generate_simulated_design(metadata)
data_dict = utils.compute_response(design_dict)

# Run the Bayesian discrete choice model
MODEL = utils.get_model()
FIT = utils.fit_model_to_data(MODEL, data_dict)

print(FIT)

### END ###
