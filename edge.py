import cv2
image=cv2.imread("image1.jpg")
image=cv2.resize(image,(1200,600))
if image is None:
    print("failed")
else:    
    cv2.imshow("Original image",image)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    sobel_x=cv2.Sobel(image,cv2.CV_64F,1,0,ksize=3)
    sobel_y=cv2.Sobel(image,cv2.CV_64F,0,1,ksize=3)
    sobel_edges=cv2.magnitude(sobel_x,sobel_y)
    sobel_edges=cv2.normalize(sobel_edges,None,0,255,cv2.NORM_MINMAX,dtype=cv2.CV_8U)
    laplacian_edges=cv2.Laplacian(image,cv2.CV_64F)
    laplacian_edges=cv2.normalize(laplacian_edges,None,0,255,cv2.NORM_MINMAX,dtype=cv2.CV_8U)
    gaussian_blur=cv2.GaussianBlur(image,(5,5),0)
    image_titles=["sobel", "laplacian", "gaussian"]
    filter=[sobel_edges,laplacian_edges,gaussian_blur]
    for title,filter in zip(image_titles,filter):
        cv2.imshow(title,filter)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
cv2.waitKey(0)
cv2.destroyAllWindows()
