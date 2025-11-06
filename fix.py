import re

# Read the file
with open('Sources/SwiftCache/SwiftCache.swift', 'r') as f:
    content = f.read()

# Fix 1: Replace the problematic AppKit code in storeInMemory (around line 204-208)
old_pattern1 = r'#elseif canImport\(AppKit\)\s+guard let cgImage = image\.cgImage\(forProposedRect: nil, context: nil, hints: nil\),\s+let bitmapRep: NSBitmapImageRep\s+bitmapRep = NSBitmapImageRep\(cgImage: cgImage\),\s+let imageData = bitmapRep\.representation\(using: \.jpeg, properties: \[:\]\) else \{ return \}'

new_code1 = '''#elseif canImport(AppKit)
        guard let cgImage = image.cgImage(forProposedRect: nil, context: nil, hints: nil) else { return }
        let bitmapRep = NSBitmapImageRep(cgImage: cgImage)
        guard let imageData = bitmapRep.representation(using: .jpeg, properties: [:]) else { return }'''

content = re.sub(old_pattern1, new_code1, content, flags=re.MULTILINE)

# Fix 2: Replace similar code in storeToDisk (around line 258-261)
old_pattern2 = r'guard let cgImage = image\.cgImage\(forProposedRect: nil, context: nil, hints: nil\),\s+let bitmapRep = NSBitmapImageRep\(cgImage: cgImage\),\s+let data = bitmapRep\.representation\(using: \.jpeg, properties: \[:\]\) else \{ return \}'

new_code2 = '''guard let cgImage = image.cgImage(forProposedRect: nil, context: nil, hints: nil) else { return }
            let bitmapRep = NSBitmapImageRep(cgImage: cgImage)
            guard let data = bitmapRep.representation(using: .jpeg, properties: [:]) else { return }'''

content = re.sub(old_pattern2, new_code2, content, flags=re.MULTILINE)

# Fix 3: Replace currentSize with sizeToClean in cleanupDiskCacheIfNeeded
content = content.replace('var currentSize = self.calculateDiskSize()', 'var sizeToClean = self.calculateDiskSize()')
content = content.replace('guard currentSize > targetSize else { break }', 'guard sizeToClean > targetSize else { break }')
content = content.replace('currentSize -= Int64(fileSize)', 'sizeToClean -= Int64(fileSize)')

# Write back
with open('Sources/SwiftCache/SwiftCache.swift', 'w') as f:
    f.write(content)

print("Fixed!")
