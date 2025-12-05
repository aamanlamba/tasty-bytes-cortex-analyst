# Deployment Guide

This guide covers deploying the project to GitHub and HuggingFace Spaces.

## GitHub Deployment

### Step 1: Create GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. Repository name: `tasty-bytes-cortex-analyst`
3. Description: `Natural language interface for customer analytics using Snowflake Cortex Analyst`
4. Set to **Public**
5. **Do not** initialize with README (we have one)
6. Click **Create repository**

### Step 2: Initialize Local Repository

```bash
cd tasty-bytes-cortex-analyst

# Initialize git
git init

# Add all files
git add .

# First commit
git commit -m "Initial commit: Tasty Bytes Cortex Analyst demo"

# Add remote (replace with your username)
git remote add origin https://github.com/YOUR_USERNAME/tasty-bytes-cortex-analyst.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Configure Repository Settings

1. Go to repository settings
2. Under **About** (right sidebar):
   - Add description
   - Add topics: `snowflake`, `cortex-analyst`, `natural-language`, `ai`, `llm`, `data-analytics`
   - Add website (HuggingFace Space URL once created)
3. Enable **Issues** for bug reports
4. Enable **Discussions** for Q&A

### Step 4: Create Demo Assets Directory

Create placeholder for demo video:

```bash
mkdir -p demo/screenshots
echo "# Demo Assets

Place your demo video (demo-video.mp4) and screenshots in this directory.

**Video Requirements:**
- Format: MP4
- Resolution: 1920x1080 (1080p)
- Duration: 3-5 minutes
- Max size: 100MB (or host externally)

**Screenshots:**
- Format: PNG or JPG
- Resolution: 1920x1080 or higher
- Include: queries, results, architecture diagram

" > demo/README.md

git add demo/README.md
git commit -m "Add demo assets directory"
git push
```

---

## HuggingFace Space Deployment

### Step 1: Create HuggingFace Account

1. Go to [huggingface.co/join](https://huggingface.co/join)
2. Sign up (free)
3. Verify your email

### Step 2: Create New Space

1. Navigate to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Click **Create new Space**
3. Configure:
   - **Owner**: Your username
   - **Space name**: `tasty-bytes-cortex-analyst`
   - **License**: MIT
   - **SDK**: Gradio
   - **Hardware**: CPU basic (free tier)
   - **Visibility**: Public
4. Click **Create Space**

### Step 3: Upload Files via Web Interface

Upload these files from the `huggingface/` directory:

1. **README.md** (the Space README)
2. **app.py** (the Gradio application)
3. **requirements.txt** (Python dependencies)

**Upload method:**

- Click **Files** tab
- Click **Add file** → **Upload files**
- Drag and drop the 3 files
- Commit message: "Initial Space deployment"
- Click **Commit**

### Step 4: (Alternative) Upload via Git

If you prefer using git:

```bash
# Clone the Space repository
git clone https://huggingface.co/spaces/YOUR_USERNAME/tasty-bytes-cortex-analyst

cd tasty-bytes-cortex-analyst

# Copy files
cp ../tasty-bytes-cortex-analyst/huggingface/* .

# Commit and push
git add .
git commit -m "Initial Space deployment"
git push
```

### Step 5: Wait for Build

- HuggingFace will automatically build your Space
- This takes 2-5 minutes
- Watch the **Logs** tab for progress
- Once complete, your Space will be live!

### Step 6: Test the Space

1. Click your Space URL: `https://huggingface.co/spaces/YOUR_USERNAME/tasty-bytes-cortex-analyst`
2. Navigate through all tabs
3. Test the interface
4. Check that all content displays correctly

### Step 7: Add Demo Video (Optional)

If your video is small enough (<100MB):

```bash
# In your Space repository
git lfs install  # Enable Git LFS for large files
git lfs track "*.mp4"
cp path/to/your/demo-video.mp4 .
git add demo-video.mp4 .gitattributes
git commit -m "Add demo video"
git push
```

Then update `app.py` to reference the video:

```python
gr.Video("demo-video.mp4", label="Watch the Demo")
```

For larger videos, host on YouTube and embed:

```python
gr.HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/YOUR_VIDEO_ID" frameborder="0" allowfullscreen></iframe>')
```

---

## Cross-Linking

### Update GitHub README

Add HuggingFace Space link at the top:

```markdown
[![HuggingFace](https://img.shields.io/badge/🤗-HuggingFace%20Space-yellow)](https://huggingface.co/spaces/YOUR_USERNAME/tasty-bytes-cortex-analyst)
```

### Update HuggingFace Space

Make sure the Space README includes GitHub link:

```markdown
**GitHub Repository**: [tasty-bytes-cortex-analyst](https://github.com/YOUR_USERNAME/tasty-bytes-cortex-analyst)
```

---

## Optional Enhancements

### GitHub

1. **Add Topics/Tags**

   - snowflake
   - cortex-analyst
   - natural-language-processing
   - llm
   - semantic-layer
   - data-analytics
   - ai-powered
2. **Create Release**

   ```bash
   git tag -a v1.0.0 -m "Initial release"
   git push origin v1.0.0
   ```

   Then create release on GitHub with release notes
3. **Add GitHub Actions** (optional)

   - Automated testing
   - Link checking
   - Documentation building

### HuggingFace

1. **Add More Datasets**

   - Sample CSV exports
   - Query result examples
2. **Enable Community Features**

   - Enable discussions
   - Add community tab
3. **Add to Collection**

   - Create a collection of data analytics tools
   - Add your Space to it

---

## Promotion Strategy

### Social Media

**LinkedIn Post Template:**

```
🚀 Excited to share my latest project: Tasty Bytes Customer Analytics!

Built with Snowflake Cortex Analyst, this demonstrates how to create a natural language interface for data analytics - no SQL required!

✨ Features:
• Ask questions in plain English
• Automatic SQL generation
• Business-friendly semantic layer
• Production-ready in 30 minutes

🔗 Try the demo: https://huggingface.co/spaces/aamanlamba/TastyBytesCortexAnalyst
📦 Full code on GitHub: https://github.com/aamanlamba/tasty-bytes-cortex-analyst

Perfect for anyone interested in #DataAnalytics #AI #Snowflake #LLM

What data would you want to query with natural language? 💭

#DataScience #AIGov #SemanticLayer #CortexAnalyst
```

**Twitter/X Post:**

```
🍔 New project: Natural language customer analytics with @SnowflakeDB Cortex Analyst

Ask "Which countries have the most customers?" and get instant insights - no SQL needed!

🔗 Demo: [Space URL]
📦 Code: [GitHub URL]

#DataAnalytics #AI #Snowflake
```

### Community Sharing

1. **Snowflake Community**

   - Post in Community Forums
   - Share in relevant LinkedIn groups
2. **HuggingFace**

   - Share in HuggingFace Discord
   - Post in relevant ML communities
3. **Reddit**

   - r/snowflake
   - r/datascience
   - r/MachineLearning
4. **Dev.to / Medium**

   - Write a detailed tutorial
   - Link to your repositories

---

## Maintenance

### Regular Updates

1. **Keep dependencies updated**

   ```bash
   pip list --outdated
   # Update requirements.txt
   ```
2. **Monitor issues**

   - Respond to GitHub issues
   - Update documentation based on questions
3. **Add new features**

   - More example queries
   - Additional semantic views
   - Enhanced visualizations

### Analytics

Track engagement:

- GitHub stars and forks
- HuggingFace Space views
- Social media engagement
- Issue/discussion activity

---

## Troubleshooting

### GitHub Issues

**Large files rejected:**

- Use Git LFS for files >100MB
- Or host videos externally (YouTube, Vimeo)

**Push rejected:**

```bash
git pull --rebase origin main
git push
```

### HuggingFace Issues

**Build failing:**

- Check logs tab
- Verify requirements.txt
- Test locally first: `python app.py`

**Space not updating:**

- Hard refresh your browser
- Clear Space cache in settings
- Rebuild the Space

---

## Success Checklist

- [ ] GitHub repository created and public
- [ ] All files committed and pushed
- [ ] Repository description and topics added
- [ ] HuggingFace Space created
- [ ] Space files uploaded and working
- [ ] Demo video added (or placeholder)
- [ ] Cross-links between GitHub and HuggingFace
- [ ] README badges added
- [ ] License file included
- [ ] Social media posts published
- [ ] Community posts shared
- [ ] Analytics tracking set up

---

**You're all set! 🎉**

Remember to engage with your community, respond to issues, and keep the project updated. Good luck!
