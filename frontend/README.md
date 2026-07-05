# FSP Frontend - React + Vite + TypeScript

## 🎨 Premium AI-Powered Dashboard Interface

Modern, responsive, enterprise-grade frontend for FSP (Future Scope Platform).

---

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- npm or yarn
- Git

### Installation

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Configure environment
cp .env.example .env

# Start development server
npm run dev
```

**Development Server**: http://localhost:5173

---

## 📁 Project Structure

```
frontend/
├── src/
│   ├── components/              # Reusable components
│   │   ├── Layout/
│   │   │   ├── Sidebar.tsx
│   │   │   ├── Navbar.tsx
│   │   │   ├── Footer.tsx
│   │   │   └── Layout.tsx
│   │   │
│   │   ├── Auth/
│   │   │   ├── LoginForm.tsx
│   │   │   ├── RegisterForm.tsx
│   │   │   ├── ProtectedRoute.tsx
│   │   │   └── AuthGuard.tsx
│   │   │
│   │   ├── Dashboard/
│   │   │   ├── DashboardCard.tsx
│   │   │   ├── StatCard.tsx
│   │   │   ├── ChartCard.tsx
│   │   │   ├── ActivityFeed.tsx
│   │   │   └── QuickStats.tsx
│   │   │
│   │   ├── AI/
│   │   │   ├── AIChatPanel.tsx
│   │   │   ├── ChatMessage.tsx
│   │   │   ├── ChatInput.tsx
│   │   │   ├── AIAgentCard.tsx
│   │   │   └── ConversationList.tsx
│   │   │
│   │   ├── Common/
│   │   │   ├── Button.tsx
│   │   │   ├── Input.tsx
│   │   │   ├── Modal.tsx
│   │   │   ├── Dropdown.tsx
│   │   │   ├── Notification.tsx
│   │   │   ├── LoadingSpinner.tsx
│   │   │   ├── Card.tsx
│   │   │   └── Badge.tsx
│   │   │
│   │   └── Forms/
│   │       ├── ProfileForm.tsx
│   │       ├── FileUpload.tsx
│   │       └── SearchBar.tsx
│   │
│   ├── pages/                   # Route pages
│   │   ├── Landing.tsx
│   │   ├── Auth/
│   │   │   ├── Login.tsx
│   │   │   ├── Register.tsx
│   │   │   ├── ForgotPassword.tsx
│   │   │   └── ResetPassword.tsx
│   │   │
│   │   ├── Dashboard/
│   │   │   ├── StudentDashboard.tsx
│   │   │   ├── FacultyDashboard.tsx
│   │   │   ├── RecruiterDashboard.tsx
│   │   │   ├── HRDashboard.tsx
│   │   │   ├── DeveloperDashboard.tsx
│   │   │   └── AdminDashboard.tsx
│   │   │
│   │   ├── Profile/
│   │   │   ├── MyProfile.tsx
│   │   │   ├── EditProfile.tsx
│   │   │   └── Settings.tsx
│   │   │
│   │   ├── AI/
│   │   │   ├── AIAgents.tsx
│   │   │   ├── AgentDetail.tsx
│   │   │   └── Conversations.tsx
│   │   │
│   │   ├── Student/
│   │   │   ├── Courses.tsx
│   │   │   ├── Assignments.tsx
│   │   │   ├── Resume.tsx
│   │   │   ├── Applications.tsx
│   │   │   └── Interviews.tsx
│   │   │
│   │   ├── Recruiter/
│   │   │   ├── JobPosts.tsx
│   │   │   ├── Applications.tsx
│   │   │   ├── Candidates.tsx
│   │   │   └── Analytics.tsx
│   │   │
│   │   └── NotFound.tsx
│   │
│   ├── services/                 # API services
│   │   ├── api.ts               # Axios instance
│   │   ├── auth.ts              # Auth APIs
│   │   ├── user.ts              # User APIs
│   │   ├── ai.ts                # AI APIs
│   │   ├── student.ts           # Student APIs
│   │   ├── recruiter.ts         # Recruiter APIs
│   │   ├── files.ts             # File APIs
│   │   └── dashboard.ts         # Dashboard APIs
│   │
│   ├── hooks/                    # Custom hooks
│   │   ├── useAuth.ts
│   │   ├── useUser.ts
│   │   ├── useForm.ts
│   │   ├── useLocalStorage.ts
│   │   ├── useAPI.ts
│   │   └── usePagination.ts
│   │
│   ├── contexts/                 # React contexts
│   │   ├── AuthContext.tsx
│   │   ├── ThemeContext.tsx
│   │   ├── NotificationContext.tsx
│   │   └── UserContext.tsx
│   │
│   ├── utils/                    # Utility functions
│   │   ├── constants.ts
│   │   ├── validators.ts
│   │   ├── formatters.ts
│   │   ├── helpers.ts
│   │   └── axios-config.ts
│   │
│   ├── styles/                   # Global styles
│   │   ├── globals.css
│   │   ├── animations.css
│   │   └── theme.css
│   │
│   ├── types/                    # TypeScript types
│   │   ├── api.ts
│   │   ├── user.ts
│   │   ├── auth.ts
│   │   ├── ai.ts
│   │   └── common.ts
│   │
│   ├── App.tsx                   # Main App component
│   ├── main.tsx                  # Entry point
│   └── vite-env.d.ts             # Vite types
│
├── public/                        # Static assets
├── .env.example                   # Environment template
├── package.json
├── tsconfig.json
├── vite.config.ts
├── tailwind.config.js
├── postcss.config.js
├── .eslintrc.cjs
├── .prettierrc
└── README.md
```

---

## 🛠️ Available Scripts

```bash
# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run tests
npm run test

# Run tests with coverage
npm run test:coverage

# Lint code
npm run lint

# Format code
npm run format

# Type check
npm run type-check
```

---

## 📦 Dependencies

### Core
- `react` - UI library
- `react-dom` - React DOM rendering
- `react-router-dom` - Routing
- `typescript` - Type safety

### Styling
- `tailwindcss` - Utility-first CSS
- `framer-motion` - Animations
- `lucide-react` - Icons

### State & Data
- `@tanstack/react-query` - Server state management
- `zustand` or `jotai` - Client state
- `axios` - HTTP client

### Forms & Validation
- `react-hook-form` - Form management
- `zod` or `yup` - Validation

### UI Components
- `headlessui` - Unstyled components
- `radix-ui` - Accessible primitives

---

## 🌐 Environment Variables

Create `.env` file:

```env
# API Configuration
VITE_API_URL=http://localhost:8000/api/v1
VITE_API_TIMEOUT=30000

# App Configuration
VITE_APP_NAME=FSP Platform
VITE_APP_VERSION=1.0.0

# Feature Flags
VITE_ENABLE_ANALYTICS=true
VITE_ENABLE_NOTIFICATIONS=true

# AI Configuration
VITE_AI_ENABLED=true
VITE_UPLOAD_MAX_SIZE=52428800
```

---

## 🎨 Styling

### Tailwind CSS

The project uses Tailwind CSS for styling with custom configuration:

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: '#3b82f6',
        secondary: '#8b5cf6',
        accent: '#ec4899',
      },
    },
  },
}
```

### CSS Modules & Global Styles

- Global styles: `src/styles/globals.css`
- Animations: `src/styles/animations.css`
- Theme: `src/styles/theme.css`

---

## 🔐 Authentication Flow

```
1. User enters credentials
   ↓
2. Submit to /api/v1/auth/login
   ↓
3. Receive access & refresh tokens
   ↓
4. Store tokens in localStorage
   ↓
5. Add token to Authorization header
   ↓
6. Access protected routes
   ↓
7. On token expiry, use refresh token
   ↓
8. Get new access token
```

### useAuth Hook

```typescript
const { user, login, logout, isAuthenticated } = useAuth();

// Login
await login(email, password);

// Logout
logout();

// Check if authenticated
if (isAuthenticated) {
  // Show protected content
}
```

---

## 🧩 Component Library

### Button Component

```typescript
<Button 
  variant="primary" 
  size="lg"
  onClick={handleClick}
>
  Click Me
</Button>
```

### Modal Component

```typescript
<Modal isOpen={isOpen} onClose={closeModal}>
  <Modal.Header>Title</Modal.Header>
  <Modal.Body>Content</Modal.Body>
  <Modal.Footer>
    <Button onClick={closeModal}>Close</Button>
  </Modal.Footer>
</Modal>
```

### Card Component

```typescript
<Card>
  <Card.Header>Title</Card.Header>
  <Card.Body>Content</Card.Body>
  <Card.Footer>Footer</Card.Footer>
</Card>
```

---

## 🎨 Pages Overview

### Landing Page
- Hero section with CTA
- Features showcase
- Testimonials
- Pricing (if applicable)
- Footer

### Login Page
- Email input
- Password input
- Remember me checkbox
- Forgot password link
- Social login (optional)
- Registration link

### Dashboard (Role-Specific)
- Statistics cards
- Charts & graphs
- Recent activities
- Quick actions
- Notifications
- AI helper panel

### AI Agents Page
- Agent list with cards
- Agent details
- Chat interface
- Conversation history
- File upload area

### Profile Page
- User information
- Avatar upload
- Edit profile form
- Password change
- Security settings
- Account preferences

---

## 🚀 Performance Optimization

### Code Splitting

```typescript
import { lazy, Suspense } from 'react';

const Dashboard = lazy(() => import('./pages/Dashboard'));

<Suspense fallback={<Loading />}>
  <Dashboard />
</Suspense>
```

### Image Optimization

```typescript
<img 
  src="image.jpg" 
  loading="lazy" 
  alt="Description"
/>
```

### Query Caching

```typescript
const { data } = useQuery(
  ['users'],
  () => fetchUsers(),
  { 
    staleTime: 5 * 60 * 1000,  // 5 minutes
    cacheTime: 10 * 60 * 1000, // 10 minutes
  }
);
```

---

## 🧪 Testing

### Unit Tests

```typescript
// components/__tests__/Button.test.tsx
import { render, screen } from '@testing-library/react';
import { Button } from '../Button';

describe('Button', () => {
  it('renders with text', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByText('Click me')).toBeInTheDocument();
  });
});
```

### Integration Tests

```typescript
// pages/__tests__/Dashboard.test.tsx
it('displays dashboard data', async () => {
  render(<Dashboard />);
  await waitFor(() => {
    expect(screen.getByText(/statistics/i)).toBeInTheDocument();
  });
});
```

---

## 🌙 Dark Mode

```typescript
const { theme, toggleTheme } = useTheme();

<button onClick={toggleTheme}>
  {theme === 'dark' ? '☀️' : '🌙'}
</button>
```

---

## 🔔 Notifications

```typescript
const { notify } = useNotification();

// Success
notify.success('Operation successful!');

// Error
notify.error('Something went wrong!');

// Info
notify.info('Information message');

// Warning
notify.warning('Warning message');
```

---

## 🚨 Error Handling

```typescript
try {
  const response = await authService.login(email, password);
  setUser(response.user);
  navigate('/dashboard');
} catch (error) {
  if (error.response?.status === 401) {
    notify.error('Invalid credentials');
  } else {
    notify.error('Login failed');
  }
}
```

---

## 📱 Responsive Design

### Breakpoints

```css
/* Mobile: < 768px */
@media (max-width: 767px) {
  /* Mobile styles */
}

/* Tablet: 768px - 1023px */
@media (min-width: 768px) and (max-width: 1023px) {
  /* Tablet styles */
}

/* Desktop: >= 1024px */
@media (min-width: 1024px) {
  /* Desktop styles */
}
```

### Mobile-First Approach

```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
  <!-- 1 column on mobile, 2 on tablet, 3 on desktop -->
</div>
```

---

## 🔗 API Integration

### Axios Instance

```typescript
// services/api.ts
import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: import.meta.env.VITE_API_TIMEOUT,
});

// Add auth token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
```

### API Service Example

```typescript
// services/auth.ts
import api from './api';

export const authService = {
  login: (email: string, password: string) =>
    api.post('/auth/login', { email, password }),
  
  register: (userData: RegisterData) =>
    api.post('/auth/register', userData),
  
  logout: () =>
    api.post('/auth/logout'),
};
```

---

## 🎯 Best Practices

### Component Organization
- One component per file
- Keep components small and focused
- Export types from component files
- Use descriptive names

### State Management
- Use Context for global state
- Use hooks for local state
- Avoid prop drilling
- Keep state close to usage

### Performance
- Use React.memo for expensive components
- Implement lazy loading
- Use code splitting
- Optimize images

### Accessibility
- Use semantic HTML
- Add ARIA labels
- Test with screen readers
- Ensure keyboard navigation

### Code Quality
- Use TypeScript strictly
- Write tests
- Use linting
- Follow consistent style

---

## 🐛 Troubleshooting

### Port 5173 already in use
```bash
# Change port in vite.config.ts
export default defineConfig({
  server: {
    port: 5174,
  },
});
```

### Dependencies not installing
```bash
rm -rf node_modules
rm package-lock.json
npm install
```

### Build fails
```bash
# Clear cache
rm -rf dist
npm run build
```

### Environment variables not loading
```bash
# Restart dev server
# Variables must be prefixed with VITE_
```

---

## 📖 Additional Resources

- [React Documentation](https://react.dev)
- [Vite Documentation](https://vitejs.dev)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [Framer Motion Docs](https://www.framer.com/motion/)

---

## 🚀 Deployment

### Build for Production

```bash
npm run build
```

This creates a `dist` folder ready for deployment.

### Deploy to Vercel

1. Push to GitHub
2. Connect repository to Vercel
3. Vercel automatically deploys on push
4. Configure environment variables in Vercel dashboard

### Deploy to Netlify

1. Connect GitHub repository
2. Set build command: `npm run build`
3. Set publish directory: `dist`
4. Deploy

---

## 📝 License

MIT License - All rights reserved

---

## 👥 Contributing

1. Create a feature branch
2. Make changes
3. Submit a pull request
4. Code review & merge

---

**Built with ❤️ for FSP Platform**
