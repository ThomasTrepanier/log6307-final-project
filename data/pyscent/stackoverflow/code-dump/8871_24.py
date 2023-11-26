def split_img_label(data_train,data_test,folder_train,folder_test):
    
    os.mkdir(folder_train)
    os.mkdir(folder_test)
    
    
    train_ind=list(data_train.index)
    test_ind=list(data_test.index)
    
    
    # Train folder
    for i in tqdm(range(len(train_ind))):
        
        os.system('cp '+data_train[train_ind[i]]+' ./'+ folder_train + '/'  +data_train[train_ind[i]].split('/')[2])
        os.system('cp '+data_train[train_ind[i]].split('.jpg')[0]+'.txt'+'  ./'+ folder_train + '/'  +data_train[train_ind[i]].split('/')[2].split('.jpg')[0]+'.txt')
    
    # Test folder
    for j in tqdm(range(len(test_ind))):
        
        os.system('cp '+data_test[test_ind[j]]+' ./'+ folder_test + '/'  +data_test[test_ind[j]].split('/')[2])
        os.system('cp '+data_test[test_ind[j]].split('.jpg')[0]+'.txt'+'  ./'+ folder_test + '/'  +data_test[test_ind[j]].split('/')[2].split('.jpg')[0]+'.txt')

