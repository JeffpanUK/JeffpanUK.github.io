# 潘俊杰（Jeff） 个人网站

一个现代化、专业的个人网站，用于展示大模型算法方向的履历、技能、项目、学术成果。

## 🌟 项目特色

- 🎨 **现代化设计**: 采用渐变色彩和动态效果，提供沉浸式用户体验
- 📱 **响应式布局**: 完美适配桌面、平板和移动设备
- 🚀 **高性能**: 优化的代码和资源加载策略
- 🔍 **SEO 友好**: 语义化的 HTML 结构和优化的内容
- 📄 **内容管理**: 易于维护和扩展的内容结构
- 🔧 **技术先进**: 使用最新的前端技术和设计原则

## 📧 联系表单功能 (EmailJS)

### EmailJS 配置方法

#### 为什么选择 EmailJS
- 完全免费的个人计划（每月 200 封邮件）
- 易于配置，无需任何后端代码
- 提供高质量的邮件服务
- 支持多种邮箱提供商
- 安全可靠，符合现代安全标准

#### 配置步骤

1. **注册 EmailJS 账号**
   - 访问：https://www.emailjs.com/
   - 注册一个免费账号（支持 Google 或 GitHub 登录）

2. **获取您的配置信息**
   - 登录后点击 "Integration" 查看您的 User ID
   - 点击 "Email Services" 添加您的邮箱服务
   - 点击 "Email Templates" 创建邮件模板

3. **配置 QQ 邮箱**
   - 在 EmailJS 中选择 "Custom SMTP" 服务
   - 填写以下信息：
     ```
     Service ID: service_qq_smtp
     Host: smtp.qq.com
     Port: 587
     Username: 2359501@qq.com
     Password: 您的 QQ 邮箱授权码
     ```

4. **创建邮件模板**
   - 主题：`联系表单 - {{subject}}`
   - 内容：
     ```
     姓名：{{name}}
     邮箱：{{email}}
     主题：{{subject}}
     消息：{{message}}
     ```

5. **更新网站代码**
   - 在 `index.html` 中更新 EmailJS 公钥和模板信息
   - 构建并部署您的网站

### 详细配置说明

请查看 `emailjs-config.md` 文件获取完整的配置步骤和常见问题解答。# GitHub Actions 配置方法

#### 1. 设置 GitHub Secrets

在项目仓库的 Settings → Secrets and variables → Actions 中添加以下 Secrets：

- **SENDER_EMAIL**：发件人邮箱地址（如：2359501@qq.com）
- **SENDER_PASSWORD**：邮箱授权码（不是密码！）
- **TO_EMAIL**：收件人邮箱地址（如：2359501@qq.com）

#### 2. 配置 QQ 邮箱授权码

1. 登录 QQ 邮箱
2. 点击右上角的 "设置" → "账户"
3. 找到 "POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务"
4. 开启 "POP3/SMTP服务" 和 "IMAP/SMTP服务"
5. 点击 "生成授权码"，按提示操作（需要通过短信验证）
6. 复制生成的授权码

#### 3. 使用方法

1. 当有用户填写联系表单时，会自动创建一个带 "contact" 标签的 Issue
2. GitHub Actions 会自动检测到新创建的 Issue 并发送邮件通知
3. 您可以在 GitHub 仓库的 Issues 页面查看所有联系信息
4. 同时会收到邮件通知

#### 功能特点

- 完全免费，不需要第三方服务
- 与 GitHub 无缝集成
- 自动创建 Issue 作为联系记录
- 邮件通知功能
- 支持添加标签和分类

#### 注意事项

- 授权码需要妥善保存，不要在代码中直接暴露
- 如果授权码过期，需要重新生成
- 确保邮箱服务未被限制

### EmailJS 配置步骤

#### 1. 注册 EmailJS 账号

1. 访问 https://www.emailjs.com/ 注册一个免费账号
2. 在左侧导航栏点击 "Email Services"
3. 点击 "Add New Service"，选择您的邮箱提供商（QQ、Gmail、Outlook 等）
4. 按照提示完成邮箱配置（需要授权码）

#### 2. 创建邮件模板

1. 在左侧导航栏点击 "Email Templates"
2. 点击 "Create New Template"
3. 修改邮件主题为：`联系表单 - {{subject}}`
4. 在邮件内容中添加以下字段：
   ```
   姓名：{{name}}
   邮箱：{{email}}
   主题：{{subject}}
   消息：{{message}}
   ```
5. 保存模板，记下来模板 ID（如：template_abc123）

#### 3. 获取配置信息

1. 在左侧导航栏点击 "Integration"
2. 找到 "Public Key"（公钥），记下来（如：user_abc123xyz）
3. 在 "Email Services" 中找到服务 ID（如：service_123xyz）

#### 4. 更新网站配置

打开 `index.html` 文件，找到以下位置并替换：

1. 在 `<head>` 标签中的 `emailjs.init` 函数：
   ```javascript
   emailjs.init("YOUR_PUBLIC_KEY"); // 替换为您的公钥
   ```

2. 在表单提交函数中的服务 ID 和模板 ID：
   ```javascript
   emailjs.sendForm('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', this)
   ```

#### 5. 测试功能

1. 在本地预览您的网站
2. 填写联系表单并提交
3. 检查您的邮箱是否收到邮件

### 重要提示

- EmailJS 免费计划每月有 200 封邮件限制，完全足够个人使用
- 如果需要更多功能，可以升级到付费计划
- 确保您的邮箱配置正确，授权码没有过期
- 如果遇到问题，检查浏览器控制台输出的错误信息

### EmailJS 配置步骤

1. **注册 EmailJS 账号**：访问 https://www.emailjs.com/ 注册免费账号
2. **添加 EmailJS 脚本**：在网站的 `<head>` 标签中添加 EmailJS 脚本：
   ```html
   <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js"></script>
   ```
3. **配置 EmailJS**：
   ```javascript
   emailjs.init("YOUR_USER_ID"); // 您的 EmailJS 公钥
   ```
4. **更新表单提交代码**：
   ```javascript
   // 使用 EmailJS 发送邮件
   emailjs.sendForm('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', this)
     .then(function(response) {
       console.log('SUCCESS!', response.status, response.text);
       alert('消息发送成功！');
       this.reset();
       window.location.href = 'https://jeffpan.net/thank-you.html';
     }, function(error) {
       console.log('FAILED...', error);
       alert('发送失败，请稍后重试');
     })
     .finally(function() {
       button.textContent = originalText;
       button.disabled = false;
     });
   ```

### 配置参数说明

- **YOUR_USER_ID**：在 EmailJS 控制台获取的公钥
- **YOUR_SERVICE_ID**：配置的邮件服务 ID（如 Gmail、Outlook 或 QQ 邮箱）
- **YOUR_TEMPLATE_ID**：创建的邮件模板 ID

### 创建邮件模板

在 EmailJS 控制台中创建一个邮件模板，包含以下字段：
- `{{name}}`：姓名
- `{{email}}`：邮箱
- `{{subject}}`：主题
- `{{message}}`：消息内容

## 📧 邮件通知配置

### 1. 设置 QQ 邮箱授权码

1. 登录 QQ 邮箱
2. 点击 "设置" -> "账户"
3. 找到 "POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务"
4. 开启 "POP3/SMTP服务" 和 "IMAP/SMTP服务"
5. 点击 "生成授权码"，按照提示操作
6. 保存生成的授权码

### 2. 设置 GitHub Secrets

1. 进入项目的 GitHub 仓库页面
2. 点击 "Settings" -> "Secrets and variables" -> "Actions"
3. 点击 "New repository secret"
4. 添加以下 Secrets：
   
   - **SENDER_EMAIL**: 您的 QQ 邮箱地址（如 2359501@qq.com）
   - **SENDER_PASSWORD**: 您刚刚生成的授权码
   - **TO_EMAIL**: 收件邮箱地址（如 2359501@qq.com）

### 3. 使用方法

- 当有新 Issue 或评论时，系统会自动发送邮件通知
- 联系表单当前使用模拟提交，如需真实邮件发送，建议使用 EmailJS 或其他服务

### 注意事项

- 授权码不是 QQ 密码，而是专门用于邮件客户端的密码
- 如果授权码过期，需要重新生成
- 确保邮箱服务未被限制

## 🚀 快速开始

### 本地开发

```bash
# 克隆仓库
git clone https://github.com/2359501/jeffpan.net.git
cd jeffpan.net

# 安装依赖
npm install

# 启动本地服务器
npm run serve

# 访问网站
# 打开浏览器访问 http://localhost:8000
```

### 构建和部署

```bash
# 构建生产版本
npm run build

# 部署到 GitHub Pages
npm run deploy
```

## 📁 项目结构

```
jeffpan.net/
├── index.html              # 主页面
├── package.json            # 项目配置
├── README.md               # 项目说明
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions 部署配置
└── dist/                   # 构建输出目录
```

## 🎯 功能模块

### 1. 个人介绍
- 姓名、职位、联系方式
- 个人简介和研究方向
- 专业技能展示

### 2. 技能特长
- 大模型技术
- 深度学习框架
- 自然语言处理
- 工具与开发

### 3. 工作经验
- **2023 - 至今**：字节跳动 - Seed，语音算法专家
- **2018 - 2023**：字节跳动 - AI Lab，语音算法工程师
- **2016 - 2018**：Cerence (Nuance)，语音算法工程师

### 4. 项目展示

#### 业务项目
- **番茄小说有声书**：从 0 到 1 搭建自动化单播、多播有声书方案，支持多种音色选择
- **豆包语音**：为豆包大模型提供语音能力，包括朗读、实时通话、唱歌和方言支持
- **剪映文本朗读**：上线抖音小姐姐、东北老铁、陕西佟掌柜等热门音色，支持方言和特色发音

#### 技术项目
- **多语种 TTS 系统**：支持中、英、日、韩、法、德、意、西、阿、越等共计15语种的语音合成系统
- **Audio Caption**：开发基于多模态大模型的音频描述生成系统，实现文本到语音的精准转换
- **方言 TTS 系统**：开发支持多种中国方言的语音合成系统，提升方言识别和合成精度

### 5. 学术成果
- 论文发表情况
- 作者、期刊、年份
- 论文链接和代码

### 6. 联系我
- 联系表单，使用模拟提交（需配置后端服务）
- 邮箱、电话、社交媒体
- 地理位置

## 🛠️ 技术栈

### 前端技术
- **HTML5**: 语义化标签和现代规范
- **CSS3**: 响应式设计、动画效果
- **JavaScript ES6+**: 交互逻辑和数据处理
- **Flexbox/Grid**: 布局系统
- **CSS Variables**: 主题切换和样式管理

### 工具和框架
- **Node.js**: 开发和构建工具
- **npm**: 包管理器
- **GitHub Pages**: 部署平台
- **GitHub Actions**: CI/CD 自动化

### 部署配置
- **CNAME**: 自定义域名配置
- **404.html**: 错误页面
- **robots.txt**: 搜索引擎优化

## 🎨 设计特色

### 视觉设计
- 渐变色彩搭配
- 卡片式布局
- 平滑滚动效果
- 粒子背景动画

### 用户体验
- 清晰的导航和信息架构
- 快速的内容加载
- 直观的交互设计
- 响应式和可访问性

## 📱 设备适配

- **桌面端**: 1024px 以上
- **平板**: 768px - 1024px
- **移动端**: 768px 以下

## 🚀 部署说明

### 1. 仓库设置
- 仓库名称: `jeffpan.net`（用于 GitHub Pages）
- 默认分支: `main`
- 启用 GitHub Pages 功能

### 2. 域名配置
- 在仓库根目录创建 `CNAME` 文件
- 内容: `jeffpan.net`
- 在域名注册商处设置 DNS 解析

### 3. 自动化部署
- 使用 GitHub Actions 自动部署
- 配置 `deploy.yml` 工作流程
- 每次推送到 main 分支自动部署

## 🔄 更新和维护

### 添加新内容
1. 修改 `index.html` 中的相应部分
2. 更新数据和内容
3. 提交到 GitHub
4. 等待自动部署

### 修改样式
1. 编辑 CSS 变量和样式
2. 预览效果
3. 提交更改

### 添加新页面
1. 创建新的 HTML 文件
2. 添加导航链接
3. 更新路由配置
4. 提交并部署

## 📄 许可证

本项目采用 MIT 许可证。

## 📞 联系方式

如有问题或建议，请通过以下方式联系：

- 邮箱: 2359501@qq.com
- GitHub: [2359501](https://github.com/2359501)

---

**网站地址**: https://jeffpan.net
**GitHub 仓库**: https://github.com/2359501/jeffpan.net
