import numpy as np

def crear_imagen(word, width, height):
    image = 255 * np.ones(shape = (height, width), dtype = np.uint8)
    image = cv2.putText(image, text = word, org = (5, 30),
        fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 0.62, color = (0, 0, 0),
        thickness = 1, lineType = cv2.LINE_AA)    
    return image

def patch_gen(num_batch, patches_tensor, word, n_patches, color_channels, patch_height, patch_width, stepsize, width, height):
    image = crear_imagen(word, width, height)
    #image = skimage.util.random_noise(image, mode='s&p')
    image = 255 - image
    image = transforms.ToPILImage()(image) # np.ndarray to PIL.Image.Image
        
    for p in range(n_patches):        
        patch = transforms.functional.crop(image, 0, 0 + p * stepsize, patch_height, patch_width) # cropping of the image into patches
        patch = transforms.ToTensor()(patch) # torch.Tensor of the patch (normalized)
        #patch = torch.from_numpy(patch) # conversion to pytorch tensor again
        patch = patch.view(1, 1, patch_height, patch_width) # CNN_model expects a 4-dimensional tensor (1 dimension for batch)
        #patch = patch.type(torch.FloatTensor) # conversion to float
        #patch = patch.cuda(0) # set to cuda
        patches_tensor[num_batch, p, 0, :, :] = patch
 
    return patches_tensor