from os import listdir
directory_root = '../input/plantdisease/'

image_list, label_list = [], []

print(" Loading images ...")
root_dir = listdir(directory_root)
for directory in root_dir :
        # remove the datastore file
        if directory == ".DS_Store" :
            root_dir.remove(directory)

for plant_folder in root_dir :
        plant_disease_folder_list = listdir(f"{directory_root}/{plant_folder}")
        
        for disease_folder in plant_disease_folder_list :
            # remove datastore from list
            if disease_folder == ".DS_Store" :
                plant_disease_folder_list.remove(disease_folder)

        for plant_disease_folder in plant_disease_folder_list:
            print(f" Processing {plant_disease_folder} ...")
            plant_disease_image_list = listdir(f"{directory_root}/{plant_folder}/{plant_disease_folder}/")
                
            for single_plant_disease_image in plant_disease_image_list :
                if single_plant_disease_image == ".DS_Store" :
                    plant_disease_image_list.remove(single_plant_disease_image)
                    
                    
            # load 200 images from each folder of dataset
            for image in plant_disease_image_list[:200]:
                image_directory = f"{directory_root}/{plant_folder}/{plant_disease_folder}/{image}"
                if image_directory.endswith(".jpg") == True or image_directory.endswith(".JPG") == True:
                    label_list.append(plant_disease_folder)
                    print("adding ",plant_disease_folder, "to the file - " ,label_list )
print(" Images are loaded")  
