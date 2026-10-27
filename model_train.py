import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

print("1. Loading Dataset...")
# Dataset load kar rahe hain (header=None kyunki humari CSV mein column names nahi hain)
df = pd.read_csv('dataset.csv', header=None)

# Agar galti se koi khali row aa gayi ho toh use hata denge
df = df.dropna()

# Pehla column label hai (A, B, Hello), baaki 63 columns coordinates hain
X = df.iloc[:, 1:].values  # Features (63 points)
y = df.iloc[:, 0].values   # Labels (Text)

print("2. Encoding Labels...")
# Computer text ('A', 'B') nahi samajhta, isliye unhe numbers (0, 1, 2) mein badal rahe hain
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)
num_classes = len(encoder.classes_)
print(f"Total Classes (Signs) found: {num_classes}")

print("3. Splitting Data into Train and Test...")
# 80% data training ke liye, aur 20% data model ka test lene ke liye
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

print("4. Building the Neural Network...")
model = tf.keras.models.Sequential([
    # Input layer (63 points)
    tf.keras.layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dropout(0.2), # Overfitting rokne ke liye
    
    # Hidden layer
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    
    # Output layer (Jitne signs hain, utne output neurons)
    tf.keras.layers.Dense(num_classes, activation='softmax')
])

print("5. Compiling & Training Model...")
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Model ko 50 baar (epochs) pure data par train kar rahe hain
history = model.fit(X_train, y_train, epochs=50, validation_data=(X_test, y_test), batch_size=32)

print("\n6. Saving the Model...")
# Trained model ko save karna
model.save('signBridge_model.h5')

# Labels ki list bhi save kar rahe hain taaki baad mein pata chale ki 0 ka matlab 'A' hai
np.save('classes.npy', encoder.classes_)

print("🎉 Model Training Complete! 'signBridge_model.h5' and 'classes.npy' saved successfully.")