# Analytics Setup Guide

Your portfolio now includes **Google Analytics 4** and **Microsoft Clarity** tracking with custom event monitoring.

## Setup Instructions

### 1. Google Analytics 4 (GA4)

**Create your GA4 property:**
1. Go to [analytics.google.com](https://analytics.google.com)
2. Click **Admin** → **Create Property**
3. Name: "Bret Lawson Portfolio"
4. Select timezone and currency
5. Click **Next** → **Create a web data stream**
6. Enter your website URL: `https://bretlawson.com`
7. Copy your **Measurement ID** (format: G-XXXXXXXXXX)

**Add your Measurement ID to index.html:**
- Open `index.html`
- Find **line 59**: `<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>`
- Replace **both instances** of `G-XXXXXXXXXX` with your actual Measurement ID
  - Line 59: In the script src
  - Line 63: In the gtag('config') call

### 2. Microsoft Clarity

**Create your Clarity project:**
1. Go to [clarity.microsoft.com](https://clarity.microsoft.com)
2. Sign in with Microsoft account (free)
3. Click **Add new project**
4. Name: "Bret Lawson Portfolio"
5. Website URL: `https://bretlawson.com`
6. Copy your **Project ID** (format: XXXXXXXXXX)

**Add your Project ID to index.html:**
- Open `index.html`
- Find **line 72**: `})(window, document, "clarity", "script", "XXXXXXXXXX");`
- Replace `XXXXXXXXXX` with your actual Clarity Project ID

## Custom Events Being Tracked

Your portfolio automatically tracks:

### GA4 Events:
- **analysis_view**: When users open analysis modal
  - Parameters: `analysis_type` (payment-analysis, llm-sql-analysis, etc.)
- **modal_close**: When users close the analysis modal
- **contact_click**: When users click contact info
  - Parameters: `contact_method` (email, phone, linkedin)
- **analysis_card_hover**: When users hover over analysis cards for 2+ seconds
  - Parameters: `analysis_name` (name of the analysis)
- **scroll_depth**: Tracks page scroll at 25%, 50%, 75%, 100%
  - Parameters: `scroll_percentage`

### Microsoft Clarity Features:
- Session recordings (watch user interactions)
- Heatmaps (see where users click and scroll)
- Automatic dead click detection
- Rage click detection
- Excessive scrolling detection

## View Your Analytics

**Google Analytics 4:**
- Dashboard: [analytics.google.com](https://analytics.google.com)
- Reports → Engagement → Events
- Reports → Engagement → Pages and screens
- Explore → Create custom reports

**Microsoft Clarity:**
- Dashboard: [clarity.microsoft.com](https://clarity.microsoft.com)
- Recordings → Watch user sessions
- Heatmaps → Click, scroll, and area heatmaps
- Dashboard → Key metrics overview

## Key Metrics to Monitor

### Traffic Analysis:
- Which analysis pages get the most views?
- What's your bounce rate vs engagement rate?
- Where do visitors come from (organic, direct, referral)?

### Engagement Insights:
- Which analysis modal is opened most?
- Do visitors click your contact info?
- How far do visitors scroll?
- Where do users hover and click?

### Conversion Tracking:
- Email clicks: Direct hiring interest
- LinkedIn clicks: Professional networking
- Phone clicks: Immediate contact attempts

## Privacy & Compliance

✅ **IP Anonymization**: Enabled in GA4 (`anonymize_ip: true`)
✅ **Privacy-Friendly**: Microsoft Clarity complies with GDPR/CCPA
✅ **No Personal Data**: Only anonymous behavioral data collected

## Troubleshooting

**Analytics not working?**
1. Verify you replaced placeholder IDs with your actual tracking IDs
2. Check browser console for errors (F12 → Console)
3. Use GA4 DebugView to see real-time events
4. Clarity typically shows data within 2 hours of setup

**Test your setup:**
1. Open your portfolio in a new incognito/private window
2. Click through different analyses
3. Click your contact info
4. In GA4: Reports → Realtime (should see your session)
5. In Clarity: Dashboard → check for recent recordings

## Questions?

Your tracking is set up to capture:
- 📊 Which analyses potential employers view most
- 📧 How many visitors reach out via contact info
- 🎯 What content drives the most engagement
- 📈 Where visitors drop off or lose interest

**All data is anonymous and helps you optimize your portfolio for maximum impact!**
