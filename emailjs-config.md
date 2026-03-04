# EmailJS 配置文件

## 获取您的 EmailJS 配置

### 1. 注册 EmailJS 账号
1. 访问：https://www.emailjs.com/
2. 点击 "Sign Up" 并填写信息
3. 验证邮箱并完成注册

### 2. 获取 User ID（公钥）
1. 登录后，点击左侧菜单的 "Integration"
2. 在 "Email Services" 页面，找到 "Public Key"（公钥）
3. 复制您的 User ID（格式：user_xxxxxxxxxxxxxxxx）

### 3. 配置 Email Service
1. 点击左侧菜单的 "Email Services"
2. 点击 "Add New Service"
3. 选择您使用的邮箱服务（QQ 邮箱建议使用 SMTP 方式）

#### QQ 邮箱 SMTP 配置
1. 登录 QQ 邮箱（https://mail.qq.com/）
2. 点击右上角 "设置" → "账户"
3. 找到 "POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务"
4. 开启 "POP3/SMTP服务" 和 "IMAP/SMTP服务"
5. 点击 "生成授权码"，按照提示操作（需要短信验证）
6. 复制生成的授权码（这是您的 SMTP 密码）

### 4. 创建邮件模板
1. 点击左侧菜单的 "Email Templates"
2. 点击 "Create New Template"
3. 在模板编辑器中，配置以下内容：

#### 邮件主题：
```
联系表单 - {{subject}}
```

#### 邮件内容：
```html
<p><strong>姓名：</strong>{{name}}</p>
<p><strong>邮箱：</strong>{{email}}</p>
<p><strong>主题：</strong>{{subject}}</p>
<p><strong>消息：</strong>{{message}}</p>
```

4. 点击 "Save" 保存模板
5. 复制模板 ID（格式：template_xxxxxxxxxxxxxxxx）

### 5. 更新网站代码
找到 `index.html` 文件中以下位置：

1. 在 `<head>` 标签中更新：
   ```javascript
   emailjs.init("YOUR_USER_ID");
   ```

2. 在表单提交函数中更新：
   ```javascript
   emailjs.sendForm('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', this)
   ```

### 6. 测试您的配置
1. 保存您的更改
2. 使用 `npm run build` 和 `npm run deploy` 部署到 GitHub Pages
3. 访问网站并测试联系表单

### 重要提示
- EmailJS 免费计划每月允许发送 200 封邮件，这对个人使用来说足够了
- 请确保不要在公共代码中暴露您的私钥或授权码
- 如果您的账户被禁用，您可以联系 EmailJS 支持获取帮助

## 常见问题解答

### 为什么没有收到邮件？
1. 检查您的邮箱是否已正确配置
2. 检查您的垃圾邮件文件夹
3. 验证您的 EmailJS 配置是否正确
4. 查看浏览器控制台是否有错误信息

### 如何防止垃圾邮件？
1. 启用 EmailJS 的 reCAPTCHA 集成
2. 在表单中添加简单的验证字段
3. 限制表单提交频率

### 如何添加附件？
1. 在模板中添加文件输入字段
2. 在 EmailJS 控制台配置相应的字段
3. 更新您的表单和邮件模板
