#Sending message from device A

compose_button = ("//android.widget.Button[@text='Compose']")
add_to_mail_address = ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.EditText")
click_on_email = ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.widget.RelativeLayout")
header = ("//android.widget.EditText[@text='Subject']")
send_button = ("com.google.android.gm:id/send")
testing_mail = ("//android.widget.TextView[@text='Testing']")

#for adding image along with the text
link_button = ("//android.widget.Button[@resource-id='com.google.android.gm:id/add_attachment']")
attach_file_button = ("//android.widget.LinearLayout[@resource-id='com.google.android.gm:id/content']")
image_file = ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.drawerlayout.widget.DrawerLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.GridView/android.widget.LinearLayout[6]/android.widget.LinearLayout")

#Receiver device locator
received_email = ("//android.view.ViewGroup[@resource-id='com.google.android.gm:id/viewified_conversation_item_view']")

received_image = ("//android.widget.TextView[@text='IMG_20241027_084235165_HDR.jpg']")
image_xpath = ("//android.widget.TextView[@text='IMG_20241027_084235165_HDR.jpg']")

#For device_a
navigation_bar = ("//android.widget.ImageButton[@content-desc='Open navigation drawer']")
sent_button = ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[9]")
sent_mail_click = ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]")
image_click = ("//android.widget.ImageView[@content-desc='Preview of IMG_20241027_084235165_HDR.jpg']")



























