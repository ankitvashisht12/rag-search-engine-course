# Text processing pipeline

![alt text](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/QpkclET-620x720.png)

Case Sensitivity -> Punctuations -> Tokenization -> stop words -> stemming


Case insensitivity: Convert all text to lowercase
"The Matrix" becomes "the matrix"
"HE IS HERE" becomes "he is here"
Remove punctuation: We don't care about periods, commas, etc
"Hello, world!" becomes "hello world"
"sci-fi" becomes "scifi"
Tokenization: Break text into individual words
"the matrix" becomes ["the", "matrix"]
"hello world" becomes ["hello", "world"]
Stop words: Remove common stop words that don't add much meaning
["the", "matrix"] becomes ["matrix"]
["a", "puppy"] becomes ["puppy"]
Stemming: Keep only the stem of words
["running", "jumping"] becomes ["run", "jump"]
["watching", "windmills"] becomes ["watch", "windmill"]