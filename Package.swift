// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    name: "SwiftCache",
    platforms: [
        .iOS(.v14),
        .macOS(.v12),
        .tvOS(.v14),
        .watchOS(.v7)
    ],
    products: [
        .library(
            name: "SwiftCache",
            targets: ["SwiftCache"]
        ),
    ],
    dependencies: [],
    targets: [
        .target(
            name: "SwiftCache",
            dependencies: []
        ),
        .testTarget(
            name: "SwiftCacheTests",
            dependencies: ["SwiftCache"]
        ),
    ]
)
