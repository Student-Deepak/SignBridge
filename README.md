# SignBridge: Full-Stack Video Conferencing with Real-Time Sign Language AI Translation

SignBridge is an accessible, AI-powered meeting platform engineered to enable seamless, bidirectional communication between **deaf/mute (sign language users)** and **hearing/speaking participants**.

---

## 🌟 Key Features

### 🤟 For Muted / Deaf Participants (Sign Language Users)
- **Zero-Latency In-Browser AI Tracking**: Uses MediaPipe Hands to track 21 3D landmarks at 30–60 FPS directly in the browser via WebGL.
- **Trained Neural Network Inference**: Executes the trained `signBridge` model (63 landmark features $\rightarrow$ 29 ASL classes: A–Z, space, del, nothing).
- **Temporal Gesture Stabilizer & Word Builder**: Smooths noisy video frames using rolling majority voting and hold-duration confirmation (~650ms), allowing users to comfortably spell words and sentences.
- **Auto Text-to-Speech (TTS)**: Finished words and sentences are vocalized aloud automatically using Speech Synthesis so hearing participants can hear the deaf person speak in real time.
- **Quick ASL Phrases & 15 Conversational Sentences**: Real-time 3D landmark kinematic analyzer and 1-click shortcut palette for essential daily conversations:
  1. `👋 Hello!` (Forehead/temple salute & wave)
  2. `❓ What is your name?` (Double H-hand tap or palms-up shaking)
  3. `🏷️ My name is ______.` (Flat palm over heart & name slot injection)
  4. `🤝 How are you?` (Curved hands rolling outward)
  5. `✨ I am fine.` (5-hand with thumb touching sternum)
  6. `🙏 Thank you.` (Flat hand outward from chin)
  7. `🆘 Please help me.` (Dominant fist on flat open palm lifting upwards)
  8. `😊 I am happy.` (Open hands brushing upward on chest)
  9. `🤟 I love you.` (Iconic universal ASL ILY sign: Thumb + Index + Pinky extended)
  10. `🌅 See you tomorrow.` (V-hand peace sign forward from eye/cheek)
  11. `👍 Yes` (Thumbs-up fist nodding)
  12. `👎 No` (Index + Middle tapping thumb pinch)
  13. `💔 Sorry` (Closed fist over heart in circular motion)
  14. `🤝 Nice to meet you` (Dominant palm sliding forward across other palm + index meeting)
  15. `👋 Goodbye` (Open hand waving side-to-side at shoulder height)
- **Sign Simulator & Practice Studio**: Integrated visual guide allowing users to test, practice, and demonstrate conversational signs in the pre-meeting lobby or during meetings without a physical webcam.

### 🎙️ For Normal / Hearing Participants (Speakers)
- **Live Voice Speech-to-Text (STT)**: Web Speech Recognition continuously listens to the speaker's microphone and renders real-time closed captions on screen.
- **ASL Reference Dictionary Drawer**: Complete visual directory of all 26 ASL alphabet signs and daily conversational phrases with gesture descriptions and tips so hearing participants can learn and understand sign language during meetings.

### 🎥 Modern Video Conferencing & Meeting Tools
- **WebRTC Peer-to-Peer Video Grid**: High-definition video and audio communication between meeting participants.
- **Google Meet / Zoom-Style Floating Live Caption Bar**: Animated real-time subtitle overlay displaying who is speaking or signing with distinct color tags (`[🤟 ASL Sign]` vs `[🎙️ Voice]`).
- **In-Meeting Chat**: Real-time text messaging with role tags and timestamps.
- **Meeting Transcript & Export**: Full chronological transcript of both signed and spoken dialogues with **"Export .TXT"** and **"Export JSON"** options.
- **Interactive Reactions**: Floating emojis with confetti animations (👏, 👍, ❤️, 🙌, ✨, 🔥).
- **Screen Sharing**: 1-click screen presentation.

---

## 🏗️ Architecture & ML Pipeline

```
[Webcam Stream] 
       │
       ▼
[MediaPipe Hands] ── (21 3D Landmarks: x, y, z)
       │
       ▼
[Feature Extraction] ── (63-element feature vector)
       │
       ▼
[TF.js SignBridge Model] ── (Dense 128 -> Dropout 0.2 -> Dense 64 -> Dense 29 Softmax)
       │
       ▼
[Temporal Stabilizer] ── (Hold confirmation & Word Buffer)
       ├──> [Live Captions Bar]
       ├──> [Auto Text-To-Speech]
       └──> [Socket.io Relay to Meeting Room]
```

---

## 🚀 Getting Started

### Prerequisites
- Node.js (v18+ or v20+)
- Modern web browser (Chrome, Edge, or Brave recommended for Web Speech & WebGL support)

### Option 1: Quick Launch (Windows)
Double-click `start-signbridge.bat` or run:
```powershell
.\start-signbridge.ps1
```

### Option 2: Manual Terminal Launch

#### Step 1: Start the Backend Signaling Server
```bash
cd server
npm install
npm start
```
*Server runs on `http://localhost:5000`*

#### Step 2: Start the Frontend Client
```bash
cd client
npm install
npm run dev
```
*Client runs on `http://localhost:3000`*

---

## 📁 Repository Structure

```
SignBridge-ML - Copy/
├── client/                     # React + Vite Frontend
│   ├── public/
│   │   ├── model/              # TF.js Model Files
│   │   │   ├── model.json
│   │   │   └── group1-shard1of1.bin
│   │   └── favicon.svg
│   ├── src/
│   │   ├── components/         # UI Components
│   │   │   ├── Lobby.jsx
│   │   │   ├── MeetingRoom.jsx
│   │   │   ├── VideoGrid.jsx
│   │   │   ├── SignDetectorOverlay.jsx
│   │   │   ├── LiveCaptionsBar.jsx
│   │   │   ├── ControlBar.jsx
│   │   │   ├── ChatDrawer.jsx
│   │   │   ├── AslGuideDrawer.jsx
│   │   │   └── TranscriptDrawer.jsx
│   │   ├── data/
│   │   │   ├── classes.json    # 29 ASL Model Classes
│   │   │   └── aslGuide.js     # ASL Guide & Phrases
│   │   ├── services/
│   │   │   ├── signDetection.js # TF.js Inference & Neon Canvas Overlay
│   │   │   ├── gestureStabilizer.js # Temporal Smoothing & Word Accumulation
│   │   │   ├── speechService.js # Web Speech TTS & STT
│   │   │   ├── socketService.js # Socket.IO Real-time Relay
│   │   │   └── webrtc.js        # WebRTC Peer Connections
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   └── package.json
├── server/                     # Node.js + Express + Socket.IO Backend
│   ├── index.js                # WebRTC Signaling & Room Management
│   └── package.json
├── tfjs_model/                 # Converted TensorFlow.js Model
│   ├── model.json
│   └── group1-shard1of1.bin
├── collect_data.py             # MediaPipe Dataset Collector
├── model_train.py              # Keras Training Pipeline
├── signBridge_model.h5         # Trained Keras Model
├── classes.npy                 # Class Labels
├── start-signbridge.bat        # Windows One-Click Batch Launcher
└── start-signbridge.ps1        # PowerShell Launcher
```
