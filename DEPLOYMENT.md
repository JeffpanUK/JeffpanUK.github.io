# GitHub Pages 部署指南

## 📋 准备工作

### 1. 确保您的 GitHub 账号已登录
- 打开浏览器，访问 https://github.com
- 登录您的 GitHub 账号：2359501@qq.com
- 输入密码和两步验证代码（如果需要）

### 2. 检查网络连接
- 确保网络连接稳定，能够访问 GitHub 网站
- 如果网络不稳定，尝试使用 VPN 或更换网络

## 🚀 第一步：创建 GitHub 仓库

### 1. 访问仓库创建页面
- 在浏览器中打开：https://github.com/new
- 或者点击右上角的 "+" 图标，选择 "New repository"

### 2. 填写仓库信息
- **仓库名称**: `jeffpan.net`
- **仓库描述**: `个人网站，展示大模型算法方向的履历、技能、项目、学术成果`
- **仓库可见性**: `Public`（GitHub Pages 需要公共仓库）
- **初始化选项**: 确保不勾选 "Initialize this repository with a README"
- **gitignore 模板**: 不选择（我们将提供自己的）
- **许可证**: 不选择（我们将使用 MIT 许可证）

### 3. 创建仓库
- 点击 "Create repository" 按钮
- 复制仓库的 HTTPS 地址（例如：https://github.com/2359501/jeffpan.net.git）

## 🚀 第二步：部署代码到仓库

### 1. 在您的本地环境中
- 打开终端或命令行工具
- 进入到项目目录：
  ```bash
  cd /root/.openclaw/workspace/jeffpan.net
  ```

### 2. 配置 Git 用户名和邮箱
```bash
git config --global user.name "Jeff Pan"
git config --global user.email "2359501@qq.com"
```

### 3. 添加远程仓库
```bash
git remote add origin https://github.com/2359501/jeffpan.net.git
```

### 4. 强制推送代码到仓库
```bash
git push -u origin main --force
```

### 5. 输入 GitHub 密码
- 当提示输入密码时，输入您的 GitHub 密码
- 如果需要两步验证，您会收到验证代码，在终端中输入即可

## 🚀 第三步：启用 GitHub Pages

### 1. 访问仓库设置
- 在浏览器中打开仓库页面：https://github.com/2359501/jeffpan.net
- 点击右上角的 "Settings" 按钮

### 2. 配置 Pages 设置
- 在左侧菜单中选择 "Pages"
- 在 "Build and deployment" 部分：
  - **Source**: 选择 "Deploy from a branch"
  - **Branch**: 选择 "main" 分支，文件夹选择 "/"
- 点击 "Save" 按钮

### 3. 等待部署
- GitHub 将自动构建并部署您的网站
- 通常需要几到几分钟时间，请耐心等待

## 🚀 第四步：配置自定义域名

### 1. 访问 Pages 设置页面
- 在浏览器中打开：https://github.com/2359501/jeffpan.net/settings/pages

### 2. 设置自定义域名
- 在 "Custom domain" 部分，输入您的域名：`jeffpan.net`
- 点击 "Save" 按钮
- 页面会自动更新并显示域名验证信息

### 3. 添加 CNAME 文件（可选）
- 您的项目中已经包含了一个 `CNAME` 文件，内容为 `jeffpan.net`
- 如果需要修改，您可以编辑该文件

## 🚀 第五步：验证网站

### 1. 访问您的网站
- 等待部署完成后，访问：https://jeffpan.net
- 或者访问：https://2359501.github.io/jeffpan.net

### 2. 检查网站功能
- 验证所有页面是否正常加载
- 测试导航链接是否工作
- 检查表单提交功能
- 验证响应式设计（在不同设备上测试）

## 🚀 常见问题与解决方案

### 问题 1：无法访问仓库
**解决方案**：
- 检查网络连接是否正常
- 确保 GitHub 账号已登录
- 尝试使用 HTTPS 而不是 SSH
- 如果网络不稳定，尝试使用 VPN

### 问题 2：推送代码失败
**解决方案**：
- 检查是否已正确配置 git config
- 确保远程仓库地址正确
- 尝试使用 --force 选项强制推送
- 检查是否有未提交的文件

### 问题 3：GitHub Pages 部署失败
**解决方案**：
- 检查仓库是否为公共仓库
- 确保 Pages 配置正确（分支、路径）
- 检查 Pages 部署日志
- 尝试重新部署

### 问题 4：自定义域名无法访问
**解决方案**：
- 检查域名解析是否正确
- 确保在 Pages 设置中已配置正确的域名
- 验证 DNS 记录是否生效
- 检查是否有其他域名冲突

### 问题 5：两步验证问题
**解决方案**：
- 确保收到并正确输入验证代码
- 如果没有收到验证代码，检查邮件或手机短信
- 尝试使用备用验证方法
- 联系 GitHub 支持获取帮助

## 🚀 高级设置

### 1. 启用 HTTPS
- GitHub Pages 会自动为您的自定义域名配置 HTTPS
- 确保在 Pages 设置中启用了 "Enforce HTTPS"
- 如果没有启用，HTTPS 图标可能会显示警告

### 2. 添加自定义 404 页面
- 创建一个 `404.html` 文件
- 添加您想要显示的内容
- 确保该文件位于项目根目录

### 3. 配置仓库安全设置
- 在仓库设置中，启用 "Require pull request reviews before merging"
- 启用 "Required status checks"
- 配置 "Branch protection rules"

### 4. 添加社交媒体预览
- 在 `index.html` 中添加 Open Graph 标签
- 配置 Twitter 卡片信息
- 确保使用了合适的图片大小

## 🚀 自动部署

### 使用 GitHub Actions 自动部署
- 您的项目中已经包含了一个 GitHub Actions 配置文件：`.github/workflows/deploy.yml`
- 该配置会在每次 push 到 main 分支时自动部署
- 确保在仓库设置中启用了 GitHub Actions

### 部署触发条件
- 任何推送到 main 分支的操作都会触发部署
- 包括：commit、pull request merge 等
- 部署过程通常需要几到几分钟

## 🚀 后续更新

### 如何更新网站内容
1. 修改相应的 HTML 文件
2. 提交更改到本地仓库
3. 推送到远程仓库：
   ```bash
   git add .
   git commit -m "更新内容描述"
   git push
   ```
4. 等待 GitHub Pages 自动部署

### 常见内容修改
- **个人信息**：修改 `index.html` 中的 `.hero-content` 部分
- **技能展示**：修改 `index.html` 中的 `.skills-container` 部分
- **工作经验**：修改 `index.html` 中的 `.timeline` 部分
- **项目展示**：修改 `index.html` 中的 `.projects-grid` 部分
- **学术成果**：修改 `index.html` 中的 `.publication-card` 部分
- **联系表单**：修改 `index.html` 中的 `#contactForm` 部分

## 🚀 联系支持

如果您在部署过程中遇到任何问题，请通过以下方式联系支持：
- 邮箱：2359501@qq.com
- GitHub Issues：在仓库页面创建 Issue
- 在线文档：https://github.com/2359501/jeffpan.net/wiki

---

**祝您部署顺利！** 🎉
