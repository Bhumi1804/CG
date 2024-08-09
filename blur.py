import cv2
image=cv2.imread("image1.jpg")
image=cv2.resize(image,(1200,600))
if image is None:
    print("failed")
else:    
    cv2.imshow("Original image",image)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    blur_kernel_size=(5,5)
    blurred_image=cv2.blur(image,blur_kernel_size)
    gaussian_blur_kernel_size=(5,5)
    gaussian_blurred_image=cv2.GaussianBlur(image,gaussian_blur_kernel_size,0)
    median_blur_kernel_size=5
    median_blurred_image=cv2.medianBlur(image,median_blur_kernel_size)
    image_titles=["Blurred image", "Gaussian image", "Median image"]
    filter=[blurred_image,gaussian_blurred_image,median_blurred_image]
    for title,filter in zip(image_titles,filter):
        cv2.imshow(title,filter)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
cv2.waitKey(0)
cv2.destroyAllWindows()
