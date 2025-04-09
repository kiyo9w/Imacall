Sprint 1:
DL formats: (end of week 1 = Friday Mar 7th, mid week 2 = Wednesday Mar 12, end of week 2 = Friday Mar 14).
Terms formats: (POC = proof of concept, BA = business analysis, CI/CD = continuous integration / continuous deployment,...)
“”””
Minh (Designer, Front End):
	•	React Setup: initialize the React project using Create React App. Set up a basic folder structure (e.g., /src/components, /src/pages). DL: commit initial code to Git by end of week 1.
          End Goal: Set up a solid base for frontend development.
	•	Figma Design: create wireframes for the Login, Chat, and Voice Call screens using Figma. DL: deliver the Figma project link by mid week 2.
          End Goal: Finalize clear UI wireframes to guide design.

Mui (Backend, BA, Database):
	•	BA Tasks: write detailed user stories with acceptance criteria and a prioritized list (must-have vs. nice-to-have) in a Markdown file (Google Docs or .md). DL: end of week 1.
          End Goal: Deliver a clear and prioritized BA document.
	•	Backend Setup: set up a Node.js Express backend. Create the project, install express and cors, and build a basic server (server.js) listening on port 5000. DL: end of week 2.
          End Goal: Launch a working backend server on port 5000.
	•	POC Collaboration: work with Duy to create a Python script to call the OpenAI API and expose a test endpoint (/api/test-openai). DL: end of week 2.
          End Goal: Demonstrate a working OpenAI API test endpoint.

Duy (Backend, Tester):
	•	Test Strategy: Define the initial test strategy and document test cases for login, chat, and API endpoints in a Markdown test plan. DL: end of week 1.
          End Goal: Provide an actionable test plan.
	•	POC for Voice API: Develop a Python script to call the ElevenLabs API and create a basic endpoint (/api/test-voice). Verify functionality using Postman and report results. DL: end of week 2.
          End Goal: Confirm a working voice API endpoint.
	•	Collaboration: Work with Mui on API integration tasks.
          End Goal: Ensure smooth API integration.

Trung (Project Manager):
	•	Meeting: 
		Organize a meeting to walk everyone through project scope, roles, tools, tech stack, and roadmap. Finalize project requirements, user stories, and acceptance criteria by end of Week 1, 2.
          End Goal: Achieve full team alignment on scope, roles, and roadmap.
	•	Git & CI/CD Oversight: Ensure the Git repository is structured (frontend and backend folders) and set up a CI/CD pipeline using GitHub Actions (create .github/workflows/ci.yml) to run basic tests on code pushes. Confirm pipeline functionality by end of week 1.
          End Goal: Set up a reliable Git structure and CI/CD pipeline.
	•	Review & Feedback: Consolidate documentation, designs, and code; review and provide feedback to the team.
          End Goal: Maintain high quality through timely reviews and feedback.

Sprint 1:
Các thời hạn (DL): (Cuối tuần 1 = Thứ Sáu ngày 7/3, giữa tuần 2 = Thứ Tư ngày 12/3, cuối tuần 2 = Thứ Sáu ngày 14/3).
Các thuật ngữ sử dụng: (POC = bản thử nghiệm khả thi, BA = phân tích nghiệp vụ, CI/CD = tích hợp liên tục / triển khai liên tục,...)

Minh (Designer, Front End):
	•	Cài đặt React: Khởi tạo dự án React bằng Create React App, thiết lập cấu trúc thư mục cơ bản (vd: /src/components, /src/pages). DL: commit mã nguồn ban đầu lên Git trước cuối tuần 1.
          Mục tiêu: Đặt nền tảng cho phát triển frontend.
	•	Thiết kế trên Figma: tạo wireframe cho các màn hình Login, Chat và Voice Call trên Figma. DL: gửi liên kết dự án Figma trước giữa tuần 2.
          Mục tiêu: Hoàn thiện wireframe UI rõ ràng cho thiết kế.

Mui (Backend, BA, Database):
	•	Công việc BA: Viết các user story chi tiết, tiêu chí chấp nhận và danh sách ưu tiên (must-have và nice-to-have) dưới dạng file Markdown (Google Docs hoặc .md). DL: cuối tuần 1.
          Mục tiêu: Cung cấp tài liệu BA rõ ràng và ưu tiên.
	•	Cài đặt Backend: Thiết lập backend sử dụng Node.js và Express. Khởi tạo dự án, cài đặt express, cors và xây dựng server cơ bản (server.js) chạy trên cổng 5000. DL: cuối tuần 2.
          Mục tiêu: Triển khai server backend hoạt động trên cổng 5000.
	•	POC phối hợp: Phối hợp cùng Duy viết một script Python gọi OpenAI API và tạo một endpoint thử nghiệm (/api/test). DL: cuối tuần 2.
          Mục tiêu: Tạo endpoint thử nghiệm OpenAI API thành công.

Duy (Phát triển API, kiểm thử):
	•	Tạo POC: Viết script Python gọi ElevenLabs API, thiết lập endpoint cơ bản (/api/test-voice). Kiểm tra bằng Postman và báo cáo kết quả. DL: cuối tuần 2.
          Mục tiêu: Xác nhận endpoint API giọng nói hoạt động.
	•	Cộng tác: Phối hợp cùng Mui để tích hợp API.
          Mục tiêu: Đảm bảo tích hợp API mượt mà.
	•	Phối hợp: Làm việc chung với Mui trong các nhiệm vụ tích hợp API.
          Mục tiêu: Đảm bảo tích hợp API hiệu quả.

Trung (Project Manager):
	•	Team meetings:
		- Tổ chức các cuộc họp để hướng dẫn về phạm vi dự án, vai trò, công cụ, tech stack và lộ trình. Thống nhất yêu cầu dự án, user story và tiêu chí chấp nhận trước cuối tuần 1, 2.
          Mục tiêu: Đạt được sự đồng thuận về phạm vi, vai trò và lộ trình dự án.
	•	Quản lý Git & CI/CD: Đảm bảo cấu trúc kho mã Git (frontend và backend), thiết lập pipeline CI/CD bằng GitHub Actions (file .github/workflows/ci.yml) chạy kiểm thử cơ bản mỗi lần có code mới. Xác nhận hoạt động trước cuối tuần 1.
          Mục tiêu: Thiết lập Git và CI/CD ổn định.
	•	Kiểm tra & phản hồi: Rà soát tài liệu, thiết kế và mã nguồn; đưa phản hồi cho nhóm.
          Mục tiêu: Duy trì chất lượng qua kiểm tra và phản hồi kịp thời.