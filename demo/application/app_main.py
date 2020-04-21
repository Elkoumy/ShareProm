from preprocessing_old import preprocessing_partyA
from preprocessing import read_xes, endcoding_events, padding_log, building_sharemind_model
from upload_to_sharemind import upload
from submit_job_to_sharemind import submit
from parse_results import parse_results
input_dir=r"/home/sharemind/shareprom/demo/application/data"
output_dir=r"/home/sharemind/shareprom/demo/application/data"
log_dir= r"/home/sharemind/shareprom/demo/application/out3.log"
# xes_file= r"C:\Gamal Elkoumy\PhD\OneDrive - Tartu Ülikool\Secure MPC\Business Process Mining SourceCode\Datasets\Sepsis Cases - Event Log (1).xes"
xes_file=r"C:\Gamal Elkoumy\PhD\OneDrive - Tartu Ülikool\Secure MPC\Business Process Mining SourceCode\Datasets\BPI_2013.xes"
# dataset_name= "activities_10"
input_dir=r"data/"
output_dir=r"data/"
dataset_name= "max_10"
no_of_chunks=1
event_a=23
event_b=22

# preprocessing_partyB(input_dir, output_dir, dataset_name)
# upload(output_dir,dataset_name)
# submit(no_of_chunks, dataset_name, event_a, event_b ,log_dir)
# parse_results(log_dir)


data, activities_count, event_per_case=read_xes(xes_file)
# #event_per_case is going to be used when uploading the file to sharemind
encoded_data= endcoding_events(data,activities_count,0)
padded_data=padding_log(encoded_data,activities_count)
model= building_sharemind_model(activities_count, dataset_name, "party_A")

print(model)