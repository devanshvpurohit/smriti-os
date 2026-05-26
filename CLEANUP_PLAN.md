# Smriti Cleanup Plan - Step 2

## Overview
This document outlines what to keep, what to remove, and what to modify from Puter to create Smriti.

---

## 🎯 Cleanup Strategy

### Philosophy
- **Keep**: Core desktop OS framework, UI shell, window management, auth
- **Remove**: Cloud features, app store, social features, monetization
- **Modify**: Rebrand UI elements, adapt for AI document focus

---

## ✅ KEEP - Essential Puter Features

### Backend Services (src/backend/services/)
- ✅ **auth/** - Authentication system (AuthService, TokenService, OTPUtil)
- ✅ **fs/** - Filesystem service (for local file management)
- ✅ **health/** - Server health monitoring
- ✅ **socket/** - WebSocket support (for streaming)
- ✅ **selfhosted/** - Self-hosting features
- ✅ **acl/** - Access control (useful for multi-user)
- ✅ **permission/** - Permission system

### Frontend UI (src/gui/src/UI/)
- ✅ **UIWindow.js** - Window management system
- ✅ **UIDesktop.js** - Desktop environment
- ✅ **UITaskbar.js** - Taskbar
- ✅ **UIContextMenu.js** - Context menus
- ✅ **UIAlert.js** - Alert dialogs
- ✅ **UIPrompt.js** - Prompt dialogs
- ✅ **UINotification.js** - Notifications
- ✅ **UIItem.js** - File/folder items
- ✅ **UIWindowLogin.js** - Login window
- ✅ **UIWindowSignup.js** - Signup window
- ✅ **UIWindowChangePassword.js** - Password management
- ✅ **UIWindowTaskManager.js** - Task manager
- ✅ **Settings/** - Settings panel

### Frontend Core (src/gui/src/)
- ✅ **index.js** - Main entry point
- ✅ **initgui.js** - GUI initialization
- ✅ **globals.js** - Global variables
- ✅ **helpers/** - All helper functions
- ✅ **services/** - Frontend services
- ✅ **lib/** - Third-party libraries (jQuery, etc.)
- ✅ **css/** - Stylesheets
- ✅ **fonts/** - Inter font family
- ✅ **icons/** - File type icons (useful for documents)
- ✅ **i18n/** - Internationalization

---

## ❌ REMOVE - Unnecessary Puter Features

### Backend Services (src/backend/services/)
- ❌ **apps/** - App store services (AppPermissionService, RecommendedAppsService, SuggestedAppsService)
- ❌ **appIcon/** - App icon service
- ❌ **homepage/** - Puter homepage service
- ❌ **metering/** - Usage metering/billing
- ❌ **subdomain/** - Subdomain management
- ❌ **broadcast/** - Broadcasting service (unless needed for notifications)
- ❌ **notification/** - Notification service (can rebuild simpler version)

### Frontend UI (src/gui/src/UI/)
- ❌ **UIWindowPublishWebsite.js** - Website publishing
- ❌ **UIWindowPublishWorker.js** - Worker publishing
- ❌ **UIWindowMyWebsites.js** - Website management
- ❌ **UIWindowFeedback.js** - Feedback form
- ❌ **UIWindowWelcome.js** - Puter welcome screen
- ❌ **UIWindow2FASetup.js** - 2FA (can add back later if needed)
- ❌ **UIWindowAuthMe.js** - Auth.me integration
- ❌ **UIWindowCopyToken.js** - Token copying
- ❌ **UIWindowQR.js** - QR code window
- ❌ **UIQRCode.js** - QR code component
- ❌ **UIWindowManageSessions.js** - Session management
- ❌ **UIWindowSessionList.js** - Session list
- ❌ **Dashboard/** - Puter dashboard (replace with Smriti dashboard)

### Frontend Helpers (src/gui/src/helpers/)
- ❌ **socialLink.js** - Social media links
- ❌ **launch_app.js** - App launching (replace with document opening)

### Other
- ❌ **src/dev-center/** - Developer center (not needed)
- ❌ **src/docs/** - Puter documentation site
- ❌ **extensions/** - Puter-specific extensions

---

## 🔄 MODIFY - Rebrand & Adapt

### Branding Changes
- 🔄 **src/gui/src/images/logo.png** - Replace with Smriti logo
- 🔄 **src/gui/src/images/wallpaper.webp** - New wallpaper
- 🔄 **src/gui/src/favicons/** - Replace all favicons
- 🔄 **src/gui/src/manifest.json** - Update app manifest
- 🔄 **src/gui/src/index.html** - Update title, meta tags (if exists)

### UI Modifications
- 🔄 **UIDesktop.js** - Adapt for document-focused interface
- 🔄 **UITaskbar.js** - Add AI/document-specific shortcuts
- 🔄 **Settings/** - Add Smriti-specific settings (AI model, chunk size, etc.)
- 🔄 **css/style.css** - Update color scheme to Smriti branding

### Text/Strings
- 🔄 **i18n/translations/** - Replace "Puter" with "Smriti" in all translations
- 🔄 All UI strings mentioning "Puter"

---

## 🆕 ADD - New Smriti Features

### New UI Components (to create)
- 🆕 **UIWindowDocumentUpload.js** - Document upload interface
- 🆕 **UIWindowChat.js** - AI chat interface
- 🆕 **UIWindowDocumentList.js** - Indexed documents list
- 🆕 **UIWindowCitations.js** - Citation viewer
- 🆕 **UIWindowSearch.js** - Semantic search (adapt existing)
- 🆕 **UIWindowAISettings.js** - AI model settings
- 🆕 **Dashboard/SmritiDashboard.js** - New dashboard for Smriti

### New Icons
- 🆕 **icons/ai.svg** - AI icon
- 🆕 **icons/document.svg** - Document icon
- 🆕 **icons/citation.svg** - Citation icon
- 🆕 **icons/brain.svg** - Brain/memory icon
- 🆕 **icons/search-semantic.svg** - Semantic search icon

---

## 📋 Cleanup Execution Plan

### Phase 1: Safe Removals (Low Risk)
1. Delete `src/dev-center/` directory
2. Delete `src/docs/` directory
3. Delete `extensions/` directory (Puter-specific)
4. Delete backend services:
   - `src/backend/services/apps/`
   - `src/backend/services/appIcon/`
   - `src/backend/services/homepage/`
   - `src/backend/services/metering/`
   - `src/backend/services/subdomain/`

### Phase 2: UI Cleanup (Medium Risk)
1. Delete unnecessary UI windows:
   - `UIWindowPublishWebsite.js`
   - `UIWindowPublishWorker.js`
   - `UIWindowMyWebsites.js`
   - `UIWindowFeedback.js`
   - `UIWindowWelcome.js`
   - `UIWindow2FASetup.js`
   - `UIWindowAuthMe.js`
   - `UIWindowCopyToken.js`
   - `UIWindowQR.js`
   - `UIWindowManageSessions.js`
   - `UIWindowSessionList.js`
2. Delete `src/gui/src/UI/Dashboard/` (will create new one)

### Phase 3: Branding Updates (High Priority)
1. Replace logo files
2. Replace favicons
3. Update manifest.json
4. Update CSS color scheme
5. Update i18n strings

### Phase 4: Code Modifications (Careful)
1. Update `UIDesktop.js` for document focus
2. Update `UITaskbar.js` with Smriti shortcuts
3. Modify Settings panel
4. Update initialization code

---

## 🔍 Files to Audit Before Deletion

### Check Dependencies
Before deleting, verify these files aren't imported elsewhere:
- `UIWindowWelcome.js` - Check if referenced in init
- `Dashboard/` - Check if referenced in routing
- `broadcast/` - Check if used for real-time updates
- `notification/` - Check if used for alerts

### Backup Strategy
1. Create git branch: `git checkout -b cleanup-puter-features`
2. Commit after each phase
3. Test after each phase
4. Can revert if needed

---

## 📊 Size Reduction Estimate

### Before Cleanup
- Total size: ~38 MB
- Files: ~56,000 objects

### After Cleanup (Estimated)
- Remove ~5-10 MB of unnecessary code
- Remove ~5,000-10,000 files
- Cleaner, more focused codebase

---

## ✅ Verification Checklist

After cleanup, verify:
- [ ] Frontend still builds: `npm run build`
- [ ] Backend still starts: `npm start`
- [ ] Login/signup works
- [ ] Window management works
- [ ] File system works
- [ ] Settings panel works
- [ ] No broken imports
- [ ] No console errors

---

## 🎯 Success Criteria

### Cleanup Complete When:
1. ✅ All unnecessary Puter features removed
2. ✅ All "Puter" branding replaced with "Smriti"
3. ✅ Application still runs without errors
4. ✅ Core desktop OS functionality intact
5. ✅ Ready for AI feature integration
6. ✅ Codebase is cleaner and more focused

---

## 📝 Notes

### Why Keep Certain Features?
- **Auth system**: Essential for user management
- **Filesystem**: Useful for document organization
- **Window management**: Core to desktop OS experience
- **Settings**: Will adapt for AI settings
- **Permissions/ACL**: Useful for future multi-user features

### Why Remove Certain Features?
- **App store**: Not relevant for document AI
- **Website publishing**: Out of scope
- **Metering/billing**: Not needed for self-hosted
- **Social features**: Privacy-first approach
- **Developer center**: Different target audience

---

## 🚀 Next Steps After Cleanup

1. Test cleaned codebase
2. Update documentation
3. Create new Smriti UI components
4. Integrate FastAPI backend
5. Add AI features

---

**Status**: Ready to execute
**Estimated Time**: 2-3 hours
**Risk Level**: Medium (can revert via git)
