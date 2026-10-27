/**
 * Semester Hub LMS - Client-side SPA Application
 * Supports Course Dashboard, Chapter Workspace (Theory, 30-MCQ Batch Quiz, Short Answer, Essay),
 * Result & Review Mode, LocalStorage Progress, Dark/Light Mode, KaTeX, Mermaid, Highlight.js.
 */

(function () {
  'use strict';

  // --- Storage Keys ---
  const STORAGE_THEME = 'semesterhub.theme';
  const STORAGE_PROGRESS = 'semesterhub.progress.v1';

  // --- App State ---
  const state = {
    manifest: null,
    currentCourse: null,
    currentChapter: null,
    chapterData: null,
    theoryMarkdown: null,
    activeTab: 'theory', // 'theory' | 'quiz' | 'short' | 'essay'
    quiz: {
      answers: {},        // { [qId]: 'A'|'B'|'C'|'D' }
      submitted: false,
      score: 0,
      total: 0,
      filterWrongOnly: false,
      lastSubmittedTime: null
    }
  };

  // --- Course UI & Pedagogical Adaptation Profiles ---
  const COURSE_PROFILES = {
    he_qtcsdl: {
      profile_name: 'technical_database',
      short_answer: {
        title: 'Luyện tập Trả lời ngắn & Thao tác hình thức',
        intro: 'Tự gõ biểu thức đại số quan hệ, câu lệnh SQL, hoặc tính toán bao đóng trước khi bấm "Kiểm tra & Đối chiếu" để so sánh với đáp án chuẩn.',
        label: 'Nhập câu trả lời / Biểu thức ĐSQH / Câu lệnh SQL của bạn:',
        placeholder: 'Gõ câu trả lời, biểu thức hoặc câu lệnh của bạn vào đây để tự rèn luyện...',
        isMono: true
      },
      essay: {
        badge: 'Tự luận & Thiết kế',
        title: 'Bài Tập Tự Luận & Thiết Kế Lớn',
        intro: 'Bài toán tổng hợp đòi hỏi tư duy thiết kế, chứng minh, tính toán nhiều bước bám sát các thuật toán chính quy của giáo trình.'
      }
    },
    cnxhkh: {
      profile_name: 'political_theory',
      short_answer: {
        title: 'Luyện tập Trả lời ngắn & Khái niệm Cốt lõi',
        intro: 'Tự suy ngẫm, tóm tắt định nghĩa, tiền đề hoặc luận điểm chính trước khi bấm "Kiểm tra & Đối chiếu" để so sánh với đáp án chuẩn.',
        label: 'Nhập câu trả lời / Tóm tắt luận điểm của bạn:',
        placeholder: 'Gõ câu trả lời, định nghĩa hoặc tóm tắt luận điểm của bạn vào đây để tự rèn luyện...',
        isMono: false
      },
      essay: {
        badge: 'Tự luận & Phân tích lý luận',
        title: 'Bài Tập Tự Luận & Phân Tích Chuyên Sâu',
        intro: 'Đề bài tự luận tổng hợp yêu cầu phân tích quy luật khách quan, chứng minh luận điểm khoa học và liên hệ thực tiễn bám sát giáo trình chuẩn Bộ GD&ĐT.'
      }
    },
    cnpm: {
      profile_name: 'software_engineering',
      short_answer: {
        title: 'Luyện tập Trả lời ngắn & Kỹ thuật Phần mềm',
        intro: 'Tự viết User Story, ca kiểm thử, lệnh Git/CI-CD hoặc phân tích kiến trúc trước khi bấm "Kiểm tra & Đối chiếu" để so sánh với đáp án chuẩn.',
        label: 'Nhập câu trả lời / Cú pháp / Ca kiểm thử / Lệnh của bạn:',
        placeholder: 'Gõ câu trả lời, cú pháp hoặc phân tích của bạn vào đây để tự rèn luyện...',
        isMono: true
      },
      essay: {
        badge: 'Tự luận & Thiết kế Phần mềm',
        title: 'Bài Tập Tự Luận & Thiết Kế Kiến Trúc / Quy Trình',
        intro: 'Bài toán tổng hợp đòi hỏi phân tích yêu cầu SRS, thiết kế kiến trúc hệ thống, hoạch định Sprint và xây dựng chiến lược kiểm thử / CI-CD.'
      }
    },
    software_engineering: {
      profile_name: 'software_engineering',
      short_answer: {
        title: 'Luyện tập Trả lời ngắn & Kỹ thuật Phần mềm',
        intro: 'Tự viết User Story, ca kiểm thử, lệnh Git/CI-CD hoặc phân tích kiến trúc trước khi bấm "Kiểm tra & Đối chiếu" để so sánh với đáp án chuẩn.',
        label: 'Nhập câu trả lời / Cú pháp / Ca kiểm thử / Lệnh của bạn:',
        placeholder: 'Gõ câu trả lời, cú pháp hoặc phân tích của bạn vào đây để tự rèn luyện...',
        isMono: true
      },
      essay: {
        badge: 'Tự luận & Thiết kế Phần mềm',
        title: 'Bài Tập Tự Luận & Thiết Kế Kiến Trúc / Quy Trình',
        intro: 'Bài toán tổng hợp đòi hỏi phân tích yêu cầu SRS, thiết kế kiến trúc hệ thống, hoạch định Sprint và xây dựng chiến lược kiểm thử / CI-CD.'
      }
    },
    tam_ly_hoc_2: {
      profile_name: 'pedagogical_psychology',
      short_answer: {
        title: 'Luyện tập Trả lời ngắn & Khái niệm Tâm lý Sư phạm',
        intro: 'Tự suy ngẫm, định nghĩa quy luật tâm lý, đặc điểm lứa tuổi hoặc xử lý tình huống sư phạm trước khi bấm "Kiểm tra & Đối chiếu" để so sánh với đáp án chuẩn.',
        label: 'Nhập câu trả lời / Luận điểm tâm lý sư phạm của bạn:',
        placeholder: 'Gõ câu trả lời, phân tích quy luật hoặc biện pháp sư phạm của bạn vào đây để tự rèn luyện...',
        isMono: false
      },
      essay: {
        badge: 'Tự luận & Ứng dụng Sư phạm',
        title: 'Bài Tập Tự Luận & Tình Huống Sư Phạm',
        intro: 'Bài tập tự luận tổng hợp yêu cầu phân tích bản chất tâm lý lứa tuổi, đề xuất phương pháp giáo dục khoa học và giải quyết tình huống thực tiễn sư phạm.'
      }
    },
    pedagogical_psychology: {
      profile_name: 'pedagogical_psychology',
      short_answer: {
        title: 'Luyện tập Trả lời ngắn & Khái niệm Tâm lý Sư phạm',
        intro: 'Tự suy ngẫm, định nghĩa quy luật tâm lý, đặc điểm lứa tuổi hoặc xử lý tình huống sư phạm trước khi bấm "Kiểm tra & Đối chiếu" để so sánh với đáp án chuẩn.',
        label: 'Nhập câu trả lời / Luận điểm tâm lý sư phạm của bạn:',
        placeholder: 'Gõ câu trả lời, phân tích quy luật hoặc biện pháp sư phạm của bạn vào đây để tự rèn luyện...',
        isMono: false
      },
      essay: {
        badge: 'Tự luận & Ứng dụng Sư phạm',
        title: 'Bài Tập Tự Luận & Tình Huống Sư Phạm',
        intro: 'Bài tập tự luận tổng hợp yêu cầu phân tích bản chất tâm lý lứa tuổi, đề xuất phương pháp giáo dục khoa học và giải quyết tình huống thực tiễn sư phạm.'
      }
    },
    default: {
      profile_name: 'general_academic',
      short_answer: {
        title: 'Luyện tập Trả lời ngắn & Tự kiểm tra',
        intro: 'Tự ghi câu trả lời hoặc tóm tắt ý chính của bạn trước khi bấm "Kiểm tra & Đối chiếu" để so sánh với đáp án chuẩn.',
        label: 'Nhập câu trả lời của bạn:',
        placeholder: 'Gõ câu trả lời của bạn vào đây để tự rèn luyện...',
        isMono: false
      },
      essay: {
        badge: 'Tự luận & Vận dụng',
        title: 'Bài Tập Tự Luận & Giải Quyết Vấn Đề',
        intro: 'Bài tập tổng hợp đòi hỏi phân tích, chứng minh và giải quyết vấn đề nhiều bước bám sát nội dung giáo trình.'
      }
    }
  };

  function getCourseUIConfig(course) {
    if (!course) return COURSE_PROFILES.default;
    const base = COURSE_PROFILES[course.ui_profile] || COURSE_PROFILES[course.id] || COURSE_PROFILES.default;
    if (course.tabs_config) {
      return {
        ...base,
        ...course.tabs_config,
        short_answer: { ...base.short_answer, ...(course.tabs_config.short_answer || {}) },
        essay: { ...base.essay, ...(course.tabs_config.essay || {}) }
      };
    }
    return base;
  }

  // --- DOM Elements ---
  const appEl = document.getElementById('app');
  const themeToggleBtn = document.getElementById('theme-toggle');
  const dialogEl = document.getElementById('dialog');
  const dialogBody = document.getElementById('dialog-body');

  // --- Theme Toggle ---
  function initTheme() {
    const saved = localStorage.getItem(STORAGE_THEME) ||
      (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    applyTheme(saved);

    themeToggleBtn.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme') || 'light';
      const next = current === 'dark' ? 'light' : 'dark';
      applyTheme(next);
      localStorage.setItem(STORAGE_THEME, next);
    });
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    const hljsLight = document.getElementById('hljs-light');
    const hljsDark = document.getElementById('hljs-dark');
    if (hljsLight && hljsDark) {
      if (theme === 'dark') {
        hljsLight.setAttribute('disabled', 'disabled');
        hljsDark.removeAttribute('disabled');
      } else {
        hljsDark.setAttribute('disabled', 'disabled');
        hljsLight.removeAttribute('disabled');
      }
    }
    if (window.mermaid) {
      try {
        window.mermaid.initialize({
          startOnLoad: false,
          theme: theme === 'dark' ? 'dark' : 'default',
          securityLevel: 'loose'
        });
      } catch (e) {
        // ignore
      }
    }
  }

  // --- Progress Management ---
  function getProgress() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_PROGRESS)) || {};
    } catch (e) {
      return {};
    }
  }

  function saveChapterResult(courseId, chapterId, score, total) {
    const p = getProgress();
    if (!p[courseId]) p[courseId] = {};
    const existing = p[courseId][chapterId] || { bestScore: 0, total: total, attempts: 0 };
    p[courseId][chapterId] = {
      bestScore: Math.max(existing.bestScore || 0, score),
      lastScore: score,
      total: total,
      attempts: (existing.attempts || 0) + 1,
      lastDate: new Date().toISOString()
    };
    localStorage.setItem(STORAGE_PROGRESS, JSON.stringify(p));
  }

  // --- Markdown & Math Rendering ---
  function renderMarkdown(mdText) {
    if (!window.marked) return mdText;
    // Configure marked options
    window.marked.setOptions({
      gfm: true,
      breaks: true,
      highlight: function (code, lang) {
        if (window.hljs && lang && window.hljs.getLanguage(lang)) {
          try {
            return window.hljs.highlight(code, { language: lang }).value;
          } catch (e) {}
        }
        return code;
      }
    });
    return window.marked.parse(mdText);
  }

  function renderMathAndDiagrams(container) {
    if (!container) return;
    // KaTeX Auto-render
    if (window.renderMathInElement) {
      try {
        window.renderMathInElement(container, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '$', right: '$', display: false }
          ],
          throwOnError: false
        });
      } catch (err) {
        console.warn('KaTeX render error:', err);
      }
    }
    // Highlight.js
    if (window.hljs) {
      container.querySelectorAll('pre code').forEach((el) => {
        try { window.hljs.highlightElement(el); } catch (e) {}
      });
    }
    // Mermaid
    if (window.mermaid) {
      const mermaidNodes = container.querySelectorAll('.language-mermaid, pre code.language-mermaid');
      mermaidNodes.forEach((node, idx) => {
        const parent = node.closest('pre') || node;
        const code = node.textContent;
        const div = document.createElement('div');
        div.className = 'mermaid my-4 flex justify-center';
        div.textContent = code;
        parent.parentNode.replaceChild(div, parent);
      });
      try {
        window.mermaid.run({ nodes: container.querySelectorAll('.mermaid') });
      } catch (err) {
        console.warn('Mermaid render error:', err);
      }
    }
  }

  // --- Dialog Helper ---
  function showDialog(title, contentHtml, onConfirm, confirmText = 'Xác nhận', cancelText = 'Hủy') {
    dialogBody.innerHTML = `
      <h3 class="text-lg font-bold mb-2">${escapeHtml(title)}</h3>
      <div class="text-sm text-muted mb-4">${contentHtml}</div>
      <div class="flex justify-end gap-2">
        <button type="button" class="btn btn-outline btn-sm" id="dlg-cancel">${escapeHtml(cancelText)}</button>
        <button type="button" class="btn btn-primary btn-sm" id="dlg-confirm">${escapeHtml(confirmText)}</button>
      </div>
    `;
    const cancelBtn = document.getElementById('dlg-cancel');
    const confirmBtn = document.getElementById('dlg-confirm');
    cancelBtn.onclick = () => dialogEl.close();
    confirmBtn.onclick = () => {
      dialogEl.close();
      if (onConfirm) onConfirm();
    };
    dialogEl.showModal();
  }

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  // --- Data Fetching ---
  async function loadManifest() {
    if (state.manifest) return state.manifest;
    const res = await fetch('data/courses_manifest.json');
    if (!res.ok) throw new Error('Không thể tải courses_manifest.json (HTTP ' + res.status + ')');
    state.manifest = await res.json();
    return state.manifest;
  }

  async function loadChapterTheory(courseId, chapterId) {
    const res = await fetch(`data/${courseId}/${chapterId}_theory.md`);
    if (!res.ok) throw new Error('Không thể tải tệp lý thuyết (HTTP ' + res.status + ')');
    return await res.text();
  }

  async function loadChapterExercises(courseId, chapterId) {
    const res = await fetch(`data/${courseId}/${chapterId}_exercises.json`);
    if (!res.ok) throw new Error('Không thể tải ngân hàng bài tập (HTTP ' + res.status + ')');
    return await res.json();
  }

  async function loadTopic(courseId, topicFile) {
    const res = await fetch(topicFile);
    if (!res.ok) throw new Error('Không thể tải chuyên đề (HTTP ' + res.status + ')');
    return await res.text();
  }

  // ==========================================
  // --- VIEWS ---
  // ==========================================

  // --- View 1: Home Portal (#/) ---
  function renderHomePortal() {
    const manifest = state.manifest;
    const progress = getProgress();

    let coursesHtml = manifest.courses.map((course) => {
      const isActive = course.status === 'active';
      const cProg = progress[course.id] || {};
      const completedCount = Object.keys(cProg).filter((cid) => (cProg[cid].attempts || 0) > 0).length;
      const totalChapters = course.books.reduce((acc, b) => acc + (b.chapters ? b.chapters.length : 0), 0);
      const totalQuestions = course.books.reduce((acc, b) => {
        return acc + (b.chapters ? b.chapters.reduce((sum, ch) => sum + (ch.counts ? ch.counts.multiple_choice : 0), 0) : 0);
      }, 0);

      const percent = totalChapters > 0 ? Math.round((completedCount / totalChapters) * 100) : 0;

      return `
        <div class="card flex flex-col justify-between ${!isActive ? 'opacity-70' : ''}">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="badge ${isActive ? 'badge-primary' : 'badge-gray'}">${escapeHtml(course.code)}</span>
              ${isActive
                ? `<span class="badge badge-success">Sẵn sàng học</span>`
                : `<span class="badge badge-warning">Đang biên soạn</span>`}
            </div>
            <h2 class="text-xl font-bold mb-2">${escapeHtml(course.title)}</h2>
            <p class="text-sm text-muted mb-4">${escapeHtml(course.description)}</p>

            ${isActive ? `
              <div class="space-y-2 mb-4">
                <div class="flex justify-between text-xs text-muted">
                  <span>Tiến độ hoàn thành: ${completedCount}/${totalChapters} chương</span>
                  <span>${percent}%</span>
                </div>
                <div class="w-full bg-slate-200 dark:bg-slate-700 h-2 rounded-full overflow-hidden">
                  <div class="bg-indigo-600 h-2 rounded-full transition-all duration-300" style="width: ${percent}%"></div>
                </div>
                <div class="flex justify-between text-xs text-subtle pt-1">
                  <span>${totalChapters} chương</span>
                  <span>${totalQuestions}+ câu trắc nghiệm</span>
                </div>
              </div>
            ` : `
              <p class="text-xs text-subtle italic mb-4">Học liệu đang được chuyển đổi sang chuẩn LMS mới.</p>
            `}
          </div>

          <div>
            ${isActive ? `
              <a href="#/course/${course.id}" class="btn btn-primary w-full">Vào Môn Học →</a>
            ` : `
              <button disabled class="btn btn-outline w-full opacity-60 cursor-not-allowed">Chưa mở</button>
            `}
          </div>
        </div>
      `;
    }).join('');

    appEl.innerHTML = `
      <div class="py-4">
        <div class="mb-8 text-center max-w-2xl mx-auto">
          <span class="badge badge-primary mb-2">Semester Hub LMS</span>
          <h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight mb-3">Cổng Học Liệu Tương Tác</h1>
          <p class="text-muted text-base">Hệ thống ôn luyện học thuật chuẩn hóa: Tóm tắt lý thuyết, Ngân hàng 30 câu trắc nghiệm/chương, Câu hỏi ngắn & Bài tập tự luận có lời giải chi tiết.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
          ${coursesHtml}
        </div>
      </div>
    `;
  }

  // --- View 2: Course Dashboard (#/course/:course_id) ---
  function renderCourseDashboard(courseId) {
    const course = state.manifest.courses.find((c) => c.id === courseId);
    if (!course) {
      appEl.innerHTML = `<div class="card text-center py-8"><p class="text-danger-text">Không tìm thấy môn học: ${escapeHtml(courseId)}</p><a href="#/" class="btn btn-primary mt-4">Về trang chủ</a></div>`;
      return;
    }

    const progress = getProgress()[courseId] || {};
    const totalChapters = course.books.reduce((acc, b) => acc + (b.chapters ? b.chapters.length : 0), 0);
    const completedChapters = Object.keys(progress).filter((cid) => (progress[cid].attempts || 0) > 0).length;
    const avgScore = completedChapters > 0
      ? (Object.values(progress).reduce((acc, cur) => acc + (cur.bestScore || 0), 0) / completedChapters).toFixed(1)
      : 0;

    let booksHtml = course.books.map((book) => {
      const chaptersHtml = (book.chapters || []).map((ch) => {
        const chProg = progress[ch.id] || null;
        const isDone = chProg && chProg.attempts > 0;
        const bestScore = isDone ? `${chProg.bestScore}/${ch.counts.multiple_choice}` : 'Chưa thi';

        return `
          <div class="card flex flex-col justify-between hover:border-indigo-400">
            <div>
              <div class="flex items-center justify-between mb-2">
                <span class="badge badge-primary">Chương ${ch.number}</span>
                ${isDone
                  ? `<span class="badge badge-success">Điểm cao nhất: ${bestScore}</span>`
                  : `<span class="badge badge-gray">Chưa làm</span>`}
              </div>
              <h3 class="text-base font-bold mb-2">${escapeHtml(ch.title)}</h3>
              <p class="text-xs text-muted mb-4 line-clamp-2">${escapeHtml(ch.summary)}</p>
            </div>
            <div class="pt-3 border-t border-subtle flex items-center justify-between">
              <span class="text-xs text-subtle font-mono">${ch.counts.multiple_choice} câu TN</span>
              <a href="#/course/${courseId}/chapter/${ch.id}" class="btn btn-primary btn-sm">Vào Học & Thi →</a>
            </div>
          </div>
        `;
      }).join('');

      return `
        <div class="mb-10">
          <h2 class="text-xl font-bold mb-4 flex items-center gap-2">
            <span class="w-2 h-6 bg-indigo-600 rounded-sm"></span>
            ${escapeHtml(book.title)}
          </h2>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            ${chaptersHtml}
          </div>
        </div>
      `;
    }).join('');

    // Topics (Chuyên đề tổng hợp)
    let topicsHtml = '';
    if (course.topics && course.topics.length > 0) {
      const list = course.topics.map((t) => `
        <a href="#/course/${courseId}/topic/${t.id}" class="card flex items-center justify-between p-4 hover:border-indigo-400 text-decoration-none">
          <span class="text-sm font-semibold">${escapeHtml(t.title)}</span>
          <span class="text-indigo-600 text-sm">Đọc tóm tắt →</span>
        </a>
      `).join('');

      topicsHtml = `
        <div class="mt-12 pt-8 border-t border-subtle">
          <h2 class="text-xl font-bold mb-4 flex items-center gap-2">
            <span class="w-2 h-6 bg-emerald-600 rounded-sm"></span>
            Chuyên Đề Ôn Tập Tổng Hợp (Ghi chú NotebookLM)
          </h2>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
            ${list}
          </div>
        </div>
      `;
    }

    appEl.innerHTML = `
      <div>
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="#/">Trang chủ</a>
          <span class="sep">/</span>
          <span class="current">${escapeHtml(course.title)}</span>
        </nav>

        <div class="card mb-8 bg-gradient-to-r from-indigo-50/50 to-purple-50/50 dark:from-indigo-950/20 dark:to-purple-950/20">
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div>
              <span class="badge badge-primary mb-2">${escapeHtml(course.code)}</span>
              <h1 class="text-2xl sm:text-3xl font-extrabold mb-2">${escapeHtml(course.title)}</h1>
              <p class="text-sm text-muted max-w-2xl">${escapeHtml(course.description)}</p>
            </div>
            <div class="flex gap-4 md:border-l border-subtle md:pl-6">
              <div class="text-center">
                <div class="text-2xl font-black text-indigo-600">${completedChapters}/${totalChapters}</div>
                <div class="text-xs text-muted">Chương hoàn thành</div>
              </div>
              <div class="text-center">
                <div class="text-2xl font-black text-emerald-600">${avgScore}</div>
                <div class="text-xs text-muted">Điểm TB trắc nghiệm</div>
              </div>
            </div>
          </div>
        </div>

        ${booksHtml}
        ${topicsHtml}
      </div>
    `;
  }

  // --- View 2b: Topic Note Viewer (#/course/:course_id/topic/:topic_id) ---
  async function renderTopicViewer(courseId, topicId) {
    const course = state.manifest.courses.find((c) => c.id === courseId);
    const topic = (course && course.topics) ? course.topics.find((t) => t.id === topicId) : null;
    if (!topic) {
      appEl.innerHTML = `<div class="card text-center py-8"><p class="text-danger-text">Không tìm thấy chuyên đề</p><a href="#/course/${courseId}" class="btn btn-primary mt-4">Về môn học</a></div>`;
      return;
    }

    appEl.innerHTML = `<div class="loading"><span class="spinner"></span> Đang tải chuyên đề...</div>`;
    try {
      const md = await loadTopic(courseId, topic.file);
      const html = renderMarkdown(md);

      appEl.innerHTML = `
        <div>
          <nav class="breadcrumb" aria-label="Breadcrumb">
            <a href="#/">Trang chủ</a>
            <span class="sep">/</span>
            <a href="#/course/${courseId}">${escapeHtml(course.title)}</a>
            <span class="sep">/</span>
            <span class="current">${escapeHtml(topic.title)}</span>
          </nav>
          <div class="card prose max-w-4xl mx-auto" id="topic-content">
            ${html}
          </div>
        </div>
      `;
      renderMathAndDiagrams(document.getElementById('topic-content'));
    } catch (err) {
      appEl.innerHTML = `<div class="card text-center py-8"><p class="text-danger-text">${escapeHtml(err.message)}</p><a href="#/course/${courseId}" class="btn btn-primary mt-4">Về môn học</a></div>`;
    }
  }

  // --- View 3: Chapter Workspace (#/course/:course_id/chapter/:chapter_id) ---
  async function renderChapterWorkspace(courseId, chapterId, subTab = 'theory') {
    const course = state.manifest.courses.find((c) => c.id === courseId);
    let chapterMeta = null;
    for (const b of (course ? course.books : [])) {
      const ch = (b.chapters || []).find((c) => c.id === chapterId);
      if (ch) { chapterMeta = ch; break; }
    }

    if (!chapterMeta) {
      appEl.innerHTML = `<div class="card text-center py-8"><p class="text-danger-text">Không tìm thấy chương: ${escapeHtml(chapterId)}</p><a href="#/course/${courseId}" class="btn btn-primary mt-4">Về môn học</a></div>`;
      return;
    }

    appEl.innerHTML = `<div class="loading"><span class="spinner"></span> Đang nạp dữ liệu chương học & ngân hàng câu hỏi...</div>`;

    try {
      // Parallel fetch
      const [theoryMd, exercisesJson] = await Promise.all([
        loadChapterTheory(courseId, chapterId),
        loadChapterExercises(courseId, chapterId)
      ]);

      state.currentCourse = course;
      state.currentChapter = chapterMeta;
      state.theoryMarkdown = theoryMd;
      state.chapterData = exercisesJson;
      state.activeTab = subTab;

      // Reset or restore quiz state for this chapter
      if (!state.quiz.answers || state.quiz.currentChapterId !== chapterId) {
        state.quiz = {
          currentChapterId: chapterId,
          answers: {},
          submitted: false,
          score: 0,
          total: exercisesJson.multiple_choice.length,
          filterWrongOnly: false,
          lastSubmittedTime: null
        };
      }

      renderChapterLayout();
    } catch (err) {
      appEl.innerHTML = `
        <div class="card text-center py-8">
          <p class="text-danger-text mb-3">Lỗi tải dữ liệu: ${escapeHtml(err.message)}</p>
          <a href="#/course/${courseId}" class="btn btn-primary">Quay lại môn học</a>
        </div>
      `;
    }
  }

  function renderChapterLayout() {
    const course = state.currentCourse;
    const chapter = state.currentChapter;
    const data = state.chapterData;

    // All chapters in course for quick jump dropdown
    const allChapters = [];
    course.books.forEach((b) => (b.chapters || []).forEach((c) => allChapters.push(c)));

    const dropdownOptions = allChapters.map((c) => {
      let label = c.full_title || c.title;
      if (c.number && c.title) {
        if (c.id.startsWith('q1') || c.id.startsWith('q2')) {
          label = `Quyển ${c.id.startsWith('q1') ? '1' : '2'} - Chương ${c.number}: ${c.title}`;
        } else {
          label = `Chương ${c.number}: ${c.title}`;
        }
      }
      return `
        <option value="${c.id}" ${c.id === chapter.id ? 'selected' : ''}>
          ${escapeHtml(label)}
        </option>
      `;
    }).join('');

    appEl.innerHTML = `
      <div>
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="#/">Trang chủ</a>
          <span class="sep">/</span>
          <a href="#/course/${course.id}">${escapeHtml(course.title)}</a>
          <span class="sep">/</span>
          <span class="current">${escapeHtml(chapter.title)}</span>
        </nav>

        <div class="card mb-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
              <span class="badge badge-primary mb-1">${escapeHtml(chapter.full_title || chapter.title)}</span>
              <h1 class="text-xl sm:text-2xl font-extrabold">${escapeHtml(data.chapter_title || chapter.title)}</h1>
            </div>
            <div class="flex items-center gap-2">
              <label for="chapter-select" class="text-xs text-muted whitespace-nowrap">Chuyển chương:</label>
              <select id="chapter-select" class="card py-1.5 px-2.5 text-xs font-medium cursor-pointer">
                ${dropdownOptions}
              </select>
            </div>
          </div>
        </div>

        <!-- 4 Functional Tabs -->
        <div class="tabs-nav" role="tablist">
          <button type="button" class="tab-btn ${state.activeTab === 'theory' ? 'active' : ''}" data-tab="theory" role="tab">
            📖 1. Lý thuyết & Sơ đồ
          </button>
          <button type="button" class="tab-btn ${state.activeTab === 'quiz' ? 'active' : ''}" data-tab="quiz" role="tab">
            ✍️ 2. Trắc nghiệm (${data.multiple_choice.length} câu)
          </button>
          <button type="button" class="tab-btn ${state.activeTab === 'short' ? 'active' : ''}" data-tab="short" role="tab">
            💬 3. Trả lời ngắn (${data.short_answers.length} câu)
          </button>
          <button type="button" class="tab-btn ${state.activeTab === 'essay' ? 'active' : ''}" data-tab="essay" role="tab">
            📝 4. Tự luận (${data.essays.length} bài)
          </button>
        </div>

        <div id="tab-content" class="tab-pane"></div>
      </div>
    `;

    // Dropdown change listener
    document.getElementById('chapter-select').addEventListener('change', (e) => {
      window.location.hash = `#/course/${course.id}/chapter/${e.target.value}`;
    });

    // Tab buttons listener
    document.querySelectorAll('.tab-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        const tab = btn.getAttribute('data-tab');
        switchTab(tab);
      });
    });

    renderCurrentTab();
  }

  function switchTab(tabName) {
    state.activeTab = tabName;
    document.querySelectorAll('.tab-btn').forEach((btn) => {
      btn.classList.toggle('active', btn.getAttribute('data-tab') === tabName);
    });
    renderCurrentTab();
  }

  function renderCurrentTab() {
    const pane = document.getElementById('tab-content');
    if (!pane) return;

    if (state.activeTab === 'theory') {
      renderTabTheory(pane);
    } else if (state.activeTab === 'quiz') {
      if (state.quiz.submitted) {
        renderQuizResult(pane);
      } else {
        renderTabQuiz(pane);
      }
    } else if (state.activeTab === 'short') {
      renderTabShort(pane);
    } else if (state.activeTab === 'essay') {
      renderTabEssay(pane);
    }
  }

  // --- Tab 1: Theory ---
  function renderTabTheory(container) {
    const html = renderMarkdown(state.theoryMarkdown);
    container.innerHTML = `
      <div class="card prose max-w-4xl mx-auto" id="theory-prose">
        ${html}
      </div>
    `;
    renderMathAndDiagrams(document.getElementById('theory-prose'));
  }

  // --- Tab 2: Batch Quiz Engine (30 Questions) ---
  function renderTabQuiz(container) {
    const questions = state.chapterData.multiple_choice;
    const answeredCount = Object.keys(state.quiz.answers).length;
    const totalCount = questions.length;

    // Palette numbers
    const paletteHtml = questions.map((q, idx) => {
      const isAnswered = !!state.quiz.answers[q.id];
      return `
        <button type="button" class="palette-btn ${isAnswered ? 'answered' : ''}" data-qid="${q.id}" title="Câu ${idx + 1}">
          ${idx + 1}
        </button>
      `;
    }).join('');

    // Question List
    const questionsHtml = questions.map((q, idx) => {
      const userChoice = state.quiz.answers[q.id] || null;
      const letters = ['A', 'B', 'C', 'D'];

      const optionsHtml = letters.map((letter) => {
        const text = q.options[letter] || '';
        const isChecked = userChoice === letter;
        return `
          <label class="option-label ${isChecked ? 'selected' : ''}">
            <input type="radio" name="q_${q.id}" value="${letter}" ${isChecked ? 'checked' : ''} data-qid="${q.id}">
            <div class="flex-1">
              <span class="font-bold text-indigo-600 mr-2">${letter}.</span>
              <span class="opt-text">${escapeHtml(text)}</span>
            </div>
          </label>
        `;
      }).join('');

      return `
        <div class="card mb-6 scroll-mt-24" id="question-${q.id}">
          <div class="flex items-center justify-between mb-3">
            <span class="text-sm font-bold text-indigo-600">Câu ${idx + 1}/${totalCount}</span>
            <span class="badge ${q.difficulty === 'hard' ? 'badge-danger' : q.difficulty === 'medium' ? 'badge-warning' : 'badge-primary'}">
              ${q.difficulty === 'hard' ? 'Vận dụng cao' : q.difficulty === 'medium' ? 'Vận dụng' : 'Nhận biết'}
            </span>
          </div>
          <div class="q-title font-semibold text-base mb-4">${escapeHtml(q.question)}</div>
          <div class="options-group">${optionsHtml}</div>
        </div>
      `;
    }).join('');

    container.innerHTML = `
      <div class="grid grid-cols-1 lg:grid-cols-4 gap-6 items-start">
        <!-- Main Quiz Form (3 Cols) -->
        <div class="lg:col-span-3">
          <div class="bg-indigo-50/50 dark:bg-indigo-950/20 border border-indigo-200 dark:border-indigo-800 rounded-lg p-4 mb-6 flex flex-col sm:flex-row items-center justify-between gap-3">
            <div class="text-sm">
              <span class="font-semibold">Quy chế thi theo lô (Batch Quiz):</span>
              <span class="text-muted">Chọn phương án cho cả ${totalCount} câu rồi bấm "Nộp bài & Chấm điểm" để xem điểm số và lời giải chi tiết.</span>
            </div>
            <button type="button" class="btn btn-primary btn-sm whitespace-nowrap btn-submit-quiz">
              Nộp bài & Chấm điểm
            </button>
          </div>

          <form id="quiz-form">
            ${questionsHtml}
          </form>

          <div class="text-center py-6">
            <button type="button" class="btn btn-primary px-8 btn-submit-quiz">
              Hoàn Thành & Nộp Bài Chấm Điểm
            </button>
          </div>
        </div>

        <!-- Sticky Sidebar: Question Palette & Progress (1 Col) -->
        <div class="lg:col-span-1 lg:sticky lg:top-20">
          <div class="card">
            <div class="flex items-center justify-between mb-2">
              <h3 class="text-sm font-bold">Bảng câu hỏi</h3>
              <span class="text-xs font-mono text-muted" id="palette-count">${answeredCount}/${totalCount}</span>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full mb-3 overflow-hidden">
              <div id="palette-progress-bar" class="bg-indigo-600 h-1.5 rounded-full transition-all" style="width: ${(answeredCount / totalCount) * 100}%"></div>
            </div>
            <div class="palette-grid" id="palette-container">
              ${paletteHtml}
            </div>
            <div class="mt-4 pt-3 border-t border-subtle">
              <button type="button" class="btn btn-primary w-full text-xs btn-submit-quiz">
                Nộp bài & Chấm điểm
              </button>
            </div>
          </div>
        </div>
      </div>
    `;

    // Render KaTeX for formulas inside questions
    renderMathAndDiagrams(container);

    // Option Selection Listeners
    container.querySelectorAll('input[type="radio"]').forEach((radio) => {
      radio.addEventListener('change', (e) => {
        const qid = e.target.getAttribute('data-qid');
        const val = e.target.value;
        state.quiz.answers[qid] = val;

        // Visual selection style
        const parentGroup = e.target.closest('.options-group');
        parentGroup.querySelectorAll('.option-label').forEach((lbl) => lbl.classList.remove('selected'));
        e.target.closest('.option-label').classList.add('selected');

        // Update palette
        const palBtn = container.querySelector(`.palette-btn[data-qid="${qid}"]`);
        if (palBtn) palBtn.classList.add('answered');

        const nowCount = Object.keys(state.quiz.answers).length;
        const countEl = document.getElementById('palette-count');
        const barEl = document.getElementById('palette-progress-bar');
        if (countEl) countEl.textContent = `${nowCount}/${totalCount}`;
        if (barEl) barEl.style.width = `${(nowCount / totalCount) * 100}%`;
      });
    });

    // Palette click: Jump to question
    container.querySelectorAll('.palette-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        const qid = btn.getAttribute('data-qid');
        const el = document.getElementById(`question-${qid}`);
        if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
    });

    // Submit Quiz Listener
    container.querySelectorAll('.btn-submit-quiz').forEach((btn) => {
      btn.addEventListener('click', handleQuizSubmitPrompt);
    });
  }

  function handleQuizSubmitPrompt() {
    const questions = state.chapterData.multiple_choice;
    const totalCount = questions.length;
    const answeredCount = Object.keys(state.quiz.answers).length;
    const missing = totalCount - answeredCount;

    if (missing > 0) {
      // Find missing indices
      const missingIndices = [];
      questions.forEach((q, idx) => {
        if (!state.quiz.answers[q.id]) missingIndices.push(idx + 1);
      });
      const missingStr = missingIndices.join(', ');

      showDialog(
        'Bạn còn câu hỏi chưa trả lời!',
        `<p class="mb-2">Bạn mới làm được <strong>${answeredCount}/${totalCount}</strong> câu.</p>
         <p class="mb-2">Còn <strong>${missing} câu</strong> chưa chọn: <span class="font-mono text-indigo-600">${missingStr}</span>.</p>
         <p>Bạn có chắc chắn muốn nộp bài sớm không?</p>`,
        () => performQuizGrading(),
        'Vẫn nộp bài',
        'Làm tiếp'
      );
    } else {
      showDialog(
        'Xác nhận nộp bài',
        `<p>Bạn đã hoàn thành đủ <strong>${totalCount}/${totalCount}</strong> câu hỏi!</p>
         <p>Bấm xác nhận để hệ thống chấm điểm và hiển thị phân tích lời giải chi tiết.</p>`,
        () => performQuizGrading(),
        'Nộp bài & Chấm điểm',
        'Kiểm tra lại'
      );
    }
  }

  function performQuizGrading() {
    const questions = state.chapterData.multiple_choice;
    let score = 0;
    questions.forEach((q) => {
      if (state.quiz.answers[q.id] === q.correct_answer) {
        score++;
      }
    });

    state.quiz.submitted = true;
    state.quiz.score = score;
    state.quiz.total = questions.length;
    state.quiz.lastSubmittedTime = new Date();

    // Save to localStorage
    saveChapterResult(state.currentCourse.id, state.currentChapter.id, score, questions.length);

    renderCurrentTab();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // --- View 4: Quiz Result & Review Mode ---
  function renderQuizResult(container) {
    const questions = state.chapterData.multiple_choice;
    const score = state.quiz.score;
    const total = state.quiz.total;
    const percent = Math.round((score / total) * 100);

    let rankText = 'Cần ôn luyện thêm';
    let rankBadge = 'badge-danger';
    if (percent >= 85) { rankText = 'Xuất sắc'; rankBadge = 'badge-success'; }
    else if (percent >= 70) { rankText = 'Giỏi / Nắm vững'; rankBadge = 'badge-primary'; }
    else if (percent >= 50) { rankText = 'Khá'; rankBadge = 'badge-warning'; }

    // Palette review
    const paletteHtml = questions.map((q, idx) => {
      const userAns = state.quiz.answers[q.id];
      const isCorrect = userAns === q.correct_answer;
      return `
        <button type="button" class="palette-btn ${isCorrect ? 'correct' : 'incorrect'}" data-qid="${q.id}" title="Câu ${idx + 1}: ${isCorrect ? 'Đúng' : 'Sai'}">
          ${idx + 1}
        </button>
      `;
    }).join('');

    // Question Review Cards
    const filterWrong = state.quiz.filterWrongOnly;
    const questionsHtml = questions.map((q, idx) => {
      const userAns = state.quiz.answers[q.id] || null;
      const isCorrect = userAns === q.correct_answer;

      if (filterWrong && isCorrect) return ''; // Filter out correct ones

      const letters = ['A', 'B', 'C', 'D'];
      const optionsHtml = letters.map((letter) => {
        const text = q.options[letter] || '';
        const isUserChoice = userAns === letter;
        const isCorrectChoice = q.correct_answer === letter;

        let extraClass = '';
        let markIcon = '';
        if (isCorrectChoice) {
          extraClass = 'is-correct';
          markIcon = '✓ ';
        } else if (isUserChoice && !isCorrect) {
          extraClass = 'is-incorrect';
          markIcon = '✗ ';
        }

        return `
          <div class="option-label ${extraClass}">
            <div class="font-bold mr-2 text-sm">${letter}.</div>
            <div class="flex-1">
              <span>${markIcon}${escapeHtml(text)}</span>
            </div>
            ${isCorrectChoice ? `<span class="badge badge-success text-xs">Đáp án đúng</span>` : ''}
            ${isUserChoice && !isCorrect ? `<span class="badge badge-danger text-xs">Bạn đã chọn</span>` : ''}
          </div>
        `;
      }).join('');

      return `
        <div class="card mb-6 scroll-mt-24" id="review-question-${q.id}">
          <div class="flex items-center justify-between mb-3">
            <span class="text-sm font-bold text-indigo-600">Câu ${idx + 1}/${total}</span>
            <span class="badge ${isCorrect ? 'badge-success' : 'badge-danger'}">
              ${isCorrect ? 'Đúng (+1đ)' : 'Chưa chính xác (0đ)'}
            </span>
          </div>
          <div class="q-title font-semibold text-base mb-4">${escapeHtml(q.question)}</div>
          <div class="options-group mb-3">${optionsHtml}</div>

          <div class="explanation-box ${isCorrect ? 'success' : 'danger'}">
            <div class="font-bold text-xs uppercase tracking-wide mb-1 flex items-center gap-1.5">
              <span>💡 Giải thích chi tiết (Căn cứ giáo trình):</span>
            </div>
            <div class="text-sm prose">${renderMarkdown(q.explanation || 'Không có giải thích.')}</div>
          </div>
        </div>
      `;
    }).join('');

    container.innerHTML = `
      <div>
        <!-- Top Score Summary Banner -->
        <div class="card mb-8 border-2 ${percent >= 70 ? 'border-emerald-500' : 'border-indigo-500'}">
          <div class="flex flex-col sm:flex-row items-center justify-between gap-6">
            <div class="flex items-center gap-6">
              <div class="w-24 h-24 rounded-full flex flex-col items-center justify-center border-4 ${percent >= 70 ? 'border-emerald-500 text-emerald-600' : 'border-indigo-500 text-indigo-600'} font-black text-2xl">
                <span>${score}/${total}</span>
                <span class="text-xs font-semibold text-muted">${percent}%</span>
              </div>
              <div>
                <span class="badge ${rankBadge} mb-2">${rankText}</span>
                <h2 class="text-xl sm:text-2xl font-extrabold mb-1">Kết Quả Bài Thi Trắc Nghiệm</h2>
                <p class="text-sm text-muted">
                  Bạn trả lời đúng <strong>${score}</strong> trên tổng số <strong>${total}</strong> câu hỏi. Kỷ lục đã được lưu vào tiến độ học tập.
                </p>
              </div>
            </div>

            <div class="flex flex-wrap gap-2 w-full sm:w-auto">
              <button type="button" class="btn btn-outline btn-sm" id="btn-toggle-wrong">
                ${filterWrong ? '👁️ Xem toàn bộ 30 câu' : '🔍 Chỉ xem các câu làm sai'}
              </button>
              <button type="button" class="btn btn-primary btn-sm" id="btn-retake-quiz">
                🔄 Làm lại bài thi
              </button>
            </div>
          </div>
        </div>

        <!-- 2 Columns: Review Content + Palette -->
        <div class="grid grid-cols-1 lg:grid-cols-4 gap-6 items-start">
          <div class="lg:col-span-3">
            ${questionsHtml || `<div class="card text-center py-8"><p class="text-emerald-600 font-bold">Chúc mừng! Bạn không làm sai câu nào!</p></div>`}
          </div>

          <div class="lg:col-span-1 lg:sticky lg:top-20">
            <div class="card">
              <h3 class="text-sm font-bold mb-2">Bảng kết quả 30 câu</h3>
              <div class="palette-grid">
                ${paletteHtml}
              </div>
              <div class="mt-4 pt-3 border-t border-subtle flex justify-between text-xs text-muted">
                <span class="flex items-center gap-1"><span class="w-3 h-3 rounded-full bg-emerald-500 inline-block"></span> Đúng (${score})</span>
                <span class="flex items-center gap-1"><span class="w-3 h-3 rounded-full bg-red-500 inline-block"></span> Sai (${total - score})</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    `;

    renderMathAndDiagrams(container);

    // Retake handler
    document.getElementById('btn-retake-quiz').addEventListener('click', () => {
      showDialog(
        'Làm lại bài thi',
        '<p>Hệ thống sẽ xóa các lựa chọn hiện tại để bạn thi lại từ đầu. Điểm cao nhất trước đó vẫn được giữ trong tiến độ.</p>',
        () => {
          state.quiz.answers = {};
          state.quiz.submitted = false;
          state.quiz.score = 0;
          state.quiz.filterWrongOnly = false;
          renderCurrentTab();
          window.scrollTo({ top: 0, behavior: 'smooth' });
        },
        'Bắt đầu làm lại'
      );
    });

    // Toggle filter wrong only
    document.getElementById('btn-toggle-wrong').addEventListener('click', () => {
      state.quiz.filterWrongOnly = !state.quiz.filterWrongOnly;
      renderCurrentTab();
    });

    // Palette jump
    container.querySelectorAll('.palette-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        const qid = btn.getAttribute('data-qid');
        const el = document.getElementById(`review-question-${qid}`);
        if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
    });
  }

  // --- Tab 3: Short Answer (>= 8 Questions) ---
  function renderTabShort(container) {
    const list = state.chapterData.short_answers;
    const uiConfig = getCourseUIConfig(state.currentCourse);
    const shortCfg = uiConfig.short_answer;

    const itemsHtml = list.map((item, idx) => {
      return `
        <div class="card mb-6" id="short-item-${item.id}">
          <div class="flex items-center justify-between mb-2">
            <span class="text-sm font-bold text-indigo-600">Câu hỏi ${idx + 1}/${list.length}</span>
            <span class="badge badge-primary">Trả lời ngắn</span>
          </div>
          <div class="font-semibold text-base mb-3">${escapeHtml(item.question)}</div>
          
          <div class="mb-3">
            <label for="sa-input-${item.id}" class="block text-xs text-muted mb-1">${escapeHtml(shortCfg.label)}</label>
            <textarea id="sa-input-${item.id}" rows="2" class="card w-full text-sm ${shortCfg.isMono ? 'font-mono' : ''} p-2.5 focus:border-indigo-500" placeholder="${escapeHtml(shortCfg.placeholder)}"></textarea>
          </div>

          <div class="flex items-center justify-between">
            <button type="button" class="btn btn-outline btn-sm btn-check-short" data-sid="${item.id}">
              👁️ Kiểm tra & Đối chiếu đáp án chuẩn
            </button>
          </div>

          <div class="short-answer-box hidden mt-4 p-4 rounded-lg bg-slate-50 dark:bg-slate-900 border border-subtle" id="sa-reveal-${item.id}">
            <div class="text-xs uppercase font-bold text-emerald-600 mb-2">Đáp án chuẩn:</div>
            <div class="text-sm font-medium mb-3 prose">${renderMarkdown(item.expected_answer)}</div>
            ${item.explanation ? `
              <div class="text-xs uppercase font-bold text-muted mb-1">Phân tích & Hướng dẫn:</div>
              <div class="text-xs text-muted prose">${renderMarkdown(item.explanation)}</div>
            ` : ''}
          </div>
        </div>
      `;
    }).join('');

    container.innerHTML = `
      <div class="max-w-4xl mx-auto">
        <div class="card mb-6 bg-indigo-50/40 dark:bg-indigo-950/20 border-indigo-200 dark:border-indigo-800">
          <h2 class="text-base font-bold text-indigo-700 dark:text-indigo-400 mb-1">${escapeHtml(shortCfg.title)}</h2>
          <p class="text-xs text-muted">
            ${escapeHtml(shortCfg.intro)}
          </p>
        </div>
        ${itemsHtml}
      </div>
    `;

    renderMathAndDiagrams(container);

    // Toggle reveal
    container.querySelectorAll('.btn-check-short').forEach((btn) => {
      btn.addEventListener('click', () => {
        const sid = btn.getAttribute('data-sid');
        const box = document.getElementById(`sa-reveal-${sid}`);
        if (box) {
          box.classList.toggle('hidden');
          btn.textContent = box.classList.contains('hidden')
            ? '👁️ Kiểm tra & Đối chiếu đáp án chuẩn'
            : 'Ẩn đáp án';
          renderMathAndDiagrams(box);
        }
      });
    });
  }

  // --- Tab 4: Essay & Problem Solving (>= 4 Problems) ---
  function renderTabEssay(container) {
    const list = state.chapterData.essays;
    const uiConfig = getCourseUIConfig(state.currentCourse);
    const essayCfg = uiConfig.essay;

    const itemsHtml = list.map((item, idx) => {
      const stepsHtml = (item.solution_steps || []).map((step) => {
        return `<div class="mb-3 pl-3 border-l-2 border-indigo-500">${renderMarkdown(step)}</div>`;
      }).join('');

      return `
        <div class="card mb-6" id="essay-item-${item.id}">
          <div class="flex items-center justify-between mb-2">
            <span class="text-sm font-bold text-indigo-600">Bài toán ${idx + 1}/${list.length}</span>
            <span class="badge badge-primary">${escapeHtml(essayCfg.badge)}</span>
          </div>
          <h3 class="text-lg font-bold mb-2">${escapeHtml(item.title)}</h3>
          <div class="text-sm text-main mb-4 prose">${renderMarkdown(item.problem)}</div>

          <div>
            <button type="button" class="btn btn-outline btn-sm btn-toggle-essay" data-eid="${item.id}">
              🔍 Xem Lời Giải Từng Bước (Step-by-step Solution)
            </button>
          </div>

          <div class="essay-solution hidden mt-4 p-4 rounded-lg bg-slate-50 dark:bg-slate-900 border border-subtle" id="essay-sol-${item.id}">
            <div class="text-xs uppercase font-bold text-indigo-600 mb-3">Lời giải chi tiết từng bước:</div>
            <div class="text-sm prose">
              ${stepsHtml}
            </div>
          </div>
        </div>
      `;
    }).join('');

    container.innerHTML = `
      <div class="max-w-4xl mx-auto">
        <div class="card mb-6 bg-indigo-50/40 dark:bg-indigo-950/20 border-indigo-200 dark:border-indigo-800">
          <h2 class="text-base font-bold text-indigo-700 dark:text-indigo-400 mb-1">${escapeHtml(essayCfg.title)}</h2>
          <p class="text-xs text-muted">
            ${escapeHtml(essayCfg.intro)}
          </p>
        </div>
        ${itemsHtml}
      </div>
    `;

    renderMathAndDiagrams(container);

    // Toggle solution
    container.querySelectorAll('.btn-toggle-essay').forEach((btn) => {
      btn.addEventListener('click', () => {
        const eid = btn.getAttribute('data-eid');
        const sol = document.getElementById(`essay-sol-${eid}`);
        if (sol) {
          sol.classList.toggle('hidden');
          btn.textContent = sol.classList.contains('hidden')
            ? '🔍 Xem Lời Giải Từng Bước (Step-by-step Solution)'
            : 'Ẩn lời giải';
          renderMathAndDiagrams(sol);
        }
      });
    });
  }

  // ==========================================
  // --- HASH ROUTER ---
  // ==========================================

  async function handleRouting() {
    try {
      await loadManifest();
    } catch (err) {
      appEl.innerHTML = `<div class="card text-center py-8"><p class="text-danger-text">Lỗi nạp manifest: ${escapeHtml(err.message)}</p></div>`;
      return;
    }

    const hash = window.location.hash || '#/';

    // Route: #/
    if (hash === '#/' || hash === '' || hash === '#') {
      renderHomePortal();
      window.scrollTo(0, 0);
      return;
    }

    // Route: #/course/:course_id/chapter/:chapter_id
    const chMatch = hash.match(/^#\/course\/([a-zA-Z0-9_]+)\/chapter\/([a-zA-Z0-9_]+)(?:\/([a-zA-Z0-9_]+))?$/);
    if (chMatch) {
      const courseId = chMatch[1];
      const chapterId = chMatch[2];
      const subTab = chMatch[3] || 'theory';
      await renderChapterWorkspace(courseId, chapterId, subTab);
      return;
    }

    // Route: #/course/:course_id/topic/:topic_id
    const topicMatch = hash.match(/^#\/course\/([a-zA-Z0-9_]+)\/topic\/([a-zA-Z0-9_]+)$/);
    if (topicMatch) {
      const courseId = topicMatch[1];
      const topicId = topicMatch[2];
      await renderTopicViewer(courseId, topicId);
      window.scrollTo(0, 0);
      return;
    }

    // Route: #/course/:course_id
    const courseMatch = hash.match(/^#\/course\/([a-zA-Z0-9_]+)$/);
    if (courseMatch) {
      const courseId = courseMatch[1];
      renderCourseDashboard(courseId);
      window.scrollTo(0, 0);
      return;
    }

    // Fallback: Home
    renderHomePortal();
  }

  // --- Bootstrap ---
  window.addEventListener('hashchange', handleRouting);
  window.addEventListener('DOMContentLoaded', () => {
    initTheme();
    handleRouting();
  });

})();
