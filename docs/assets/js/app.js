// Semester Hub LMS - Modern Academic Bento & Sequential Quiz Engine
// Architecture: Single-Page Application (SPA) with Hash-based Routing & Dynamic Course Adaptation

(function () {
  'use strict';

  // --- Storage Keys ---
  const STORAGE_THEME = 'semesterhub.theme';
  const STORAGE_PROGRESS = 'semesterhub.progress.v1';
  const STORAGE_LAST_CHAPTER = 'semesterhub.last_chapter';

  // --- Central Application State ---
  const state = {
    manifest: null,
    currentCourse: null,
    currentChapter: null,
    chapterData: null,
    theoryMarkdown: null,
    activeTab: 'theory', // 'theory' | 'quiz' | 'short' | 'essay'
    quiz: {
      currentChapterId: null,
      currentIndex: 0,          // Current focused question index (0 .. total-1)
      maxUnlockedIndex: 0,      // Furthest unlocked question index
      answers: {},              // { [qId]: 'A'|'B'|'C'|'D' }
      lockedQuestions: {},      // { [qId]: true }
      mode: 'instant',          // 'instant' (Instant feedback & explanations) | 'exam' (Exam mode)
      streak: 0,                // Current consecutive correct streak
      bestStreak: 0,            // Best streak in this chapter session
      submitted: false,
      score: 0,
      total: 0,
      filterWrongOnly: false,
      lastSubmittedTime: null
    }
  };

  // --- Course Profiles & Pedagogical Adaptation ---
  const COURSE_PROFILES = {
    he_qtcsdl: {
      profile_name: 'technical_database',
      theme: {
        primary: '#4f46e5',
        secondary: '#06b6d4',
        accent: '#3b82f6',
        icon: '🗄️',
        label: 'Cơ Sở Dữ Liệu & Hệ Thống'
      },
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
      theme: {
        primary: '#e11d48',
        secondary: '#f59e0b',
        accent: '#ef4444',
        icon: '🏛️',
        label: 'Lý Luận Chính Trị & KHXH'
      },
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
      theme: {
        primary: '#7c3aed',
        secondary: '#10b981',
        accent: '#8b5cf6',
        icon: '⚙️',
        label: 'Kỹ Nghệ Phần Mềm & Quy Trình'
      },
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
      theme: {
        primary: '#0d9488',
        secondary: '#f97316',
        accent: '#14b8a6',
        icon: '🧠',
        label: 'Tâm Lý Học Lứa Tuổi & Sư Phạm'
      },
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
    giai_tich_1: {
      profile_name: 'mathematics_natural_science',
      theme: {
        primary: '#2563eb',
        secondary: '#6366f1',
        accent: '#3b82f6',
        icon: '📐',
        label: 'Toán Học & Khoa Học Cơ Bản'
      },
      short_answer: {
        title: 'Luyện tập Trả lời ngắn & Tính toán Số học',
        intro: 'Tự biến đổi đại số, tính đạo hàm, tích phân hoặc xác suất trước khi bấm "Kiểm tra & Đối chiếu" để so sánh với đáp án chuẩn.',
        label: 'Nhập kết quả tính toán / Biểu thức toán của bạn:',
        placeholder: 'Gõ câu trả lời hoặc biểu thức toán của bạn vào đây...',
        isMono: true
      },
      essay: {
        badge: 'Tự luận & Chứng minh',
        title: 'Bài Tập Tự Luận & Chứng Minh Toán Học',
        intro: 'Bài toán giải tích đòi hỏi các bước biến đổi chặt chẽ, định lý và điều kiện hội tụ bám sát giáo trình.'
      }
    },
    default: {
      profile_name: 'general_academic',
      theme: {
        primary: '#4f46e5',
        secondary: '#06b6d4',
        accent: '#6366f1',
        icon: '🎓',
        label: 'Học Thuật Đại Học'
      },
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

  // Cross-reference aliases for ui_profile identifiers
  COURSE_PROFILES.technical_database = COURSE_PROFILES.he_qtcsdl;
  COURSE_PROFILES.political_theory = COURSE_PROFILES.cnxhkh;
  COURSE_PROFILES.software_engineering = COURSE_PROFILES.cnpm;
  COURSE_PROFILES.pedagogical_psychology = COURSE_PROFILES.tam_ly_hoc_2;
  COURSE_PROFILES.mathematics_natural_science = COURSE_PROFILES.giai_tich_1;
  COURSE_PROFILES.general_academic = COURSE_PROFILES.default;

  function getCourseUIConfig(course) {
    if (!course) return COURSE_PROFILES.default;
    const base = COURSE_PROFILES[course.ui_profile] || COURSE_PROFILES[course.id] || COURSE_PROFILES.default;
    if (course.tabs_config) {
      return {
        ...base,
        ...course.tabs_config,
        theme: { ...base.theme, ...(course.tabs_config.theme || {}) },
        short_answer: { ...base.short_answer, ...(course.tabs_config.short_answer || {}) },
        essay: { ...base.essay, ...(course.tabs_config.essay || {}) }
      };
    }
    return base;
  }

  // --- Dynamic Course Color Application ---
  function applyCourseTheme(course) {
    const cfg = getCourseUIConfig(course);
    const theme = cfg.theme || COURSE_PROFILES.default.theme;
    const root = document.documentElement;
    root.style.setProperty('--course-primary', theme.primary);
    root.style.setProperty('--course-secondary', theme.secondary);
    root.style.setProperty('--course-gradient', `linear-gradient(135deg, ${theme.primary} 0%, ${theme.secondary} 100%)`);
    root.style.setProperty('--course-glow', `${theme.primary}38`);
    root.setAttribute('data-course-id', course ? course.id : 'default');
  }

  function resetCourseTheme() {
    const root = document.documentElement;
    root.style.setProperty('--course-primary', '#4f46e5');
    root.style.setProperty('--course-secondary', '#06b6d4');
    root.style.setProperty('--course-gradient', 'linear-gradient(135deg, #4f46e5 0%, #06b6d4 100%)');
    root.style.setProperty('--course-glow', 'rgba(79, 70, 229, 0.22)');
    root.removeAttribute('data-course-id');
  }

  // --- DOM Elements ---
  const appEl = document.getElementById('app');
  const themeToggleBtn = document.getElementById('theme-toggle');
  const dialogEl = document.getElementById('dialog');
  const dialogBody = document.getElementById('dialog-body');
  const readingProgressBar = document.getElementById('reading-progress-bar');

  // --- Theme Management ---
  function initTheme() {
    const saved = localStorage.getItem(STORAGE_THEME) ||
      (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    applyTheme(saved);

    if (themeToggleBtn) {
      themeToggleBtn.addEventListener('click', () => {
        const current = document.documentElement.getAttribute('data-theme') || 'light';
        const next = current === 'dark' ? 'light' : 'dark';
        applyTheme(next);
      });
    }
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem(STORAGE_THEME, theme);

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
        // Safe fallback
      }
    }
  }

  // --- Progress & LocalStorage Management ---
  function getProgress() {
    try {
      const data = localStorage.getItem(STORAGE_PROGRESS);
      return data ? JSON.parse(data) : {};
    } catch {
      return {};
    }
  }

  function saveChapterResult(courseId, chapterId, score, total) {
    const p = getProgress();
    if (!p[courseId]) p[courseId] = {};
    const existing = p[courseId][chapterId] || { bestScore: 0, total: total, attempts: 0 };
    p[courseId][chapterId] = {
      bestScore: Math.max(existing.bestScore || 0, score),
      total: total,
      attempts: (existing.attempts || 0) + 1,
      lastScore: score,
      lastAttemptAt: new Date().toISOString()
    };
    try {
      localStorage.setItem(STORAGE_PROGRESS, JSON.stringify(p));
      localStorage.setItem(STORAGE_LAST_CHAPTER, JSON.stringify({
        courseId,
        chapterId,
        timestamp: new Date().toISOString()
      }));
    } catch (e) {
      console.warn('Storage save error:', e);
    }
  }

  function recordLastVisited(courseId, chapterId) {
    try {
      localStorage.setItem(STORAGE_LAST_CHAPTER, JSON.stringify({
        courseId,
        chapterId,
        timestamp: new Date().toISOString()
      }));
    } catch (e) {
      // Ignore
    }
  }

  // --- Markdown, LaTeX & Diagrams Rendering ---
  function renderMarkdown(mdText) {
    if (!mdText) return '';
    if (window.marked) {
      marked.setOptions({
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
      return marked.parse(mdText);
    }
    return escapeHtml(mdText);
  }

  function renderMathAndDiagrams(container) {
    if (!container) return;

    // 1. KaTeX Math rendering
    if (window.renderMathInElement) {
      try {
        window.renderMathInElement(container, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '$', right: '$', display: false },
            { left: '\\(', right: '\\)', display: false },
            { left: '\\[', right: '\\]', display: true }
          ],
          throwOnError: false
        });
      } catch (err) {
        console.warn('KaTeX render warning:', err);
      }
    }

    // 2. Mermaid Diagrams rendering
    if (window.mermaid) {
      const mermaidNodes = container.querySelectorAll('.language-mermaid, pre code.language-mermaid');
      mermaidNodes.forEach((node, index) => {
        const parent = node.closest('pre') || node;
        const code = node.textContent;
        const div = document.createElement('div');
        div.className = 'mermaid my-4 flex justify-center overflow-x-auto';
        div.id = `mermaid-${Date.now()}-${index}`;
        div.textContent = code;
        parent.replaceWith(div);
      });
      try {
        window.mermaid.run({ nodes: container.querySelectorAll('.mermaid') });
      } catch (err) {
        console.warn('Mermaid render warning:', err);
      }
    }
  }

  // --- Dialog & Alert Utility ---
  function showDialog(title, contentHtml, onConfirm, confirmText = 'Xác nhận', cancelText = 'Hủy') {
    if (!dialogEl || !dialogBody) return;
    dialogBody.innerHTML = `
      <h3 class="text-lg font-bold mb-3">${escapeHtml(title)}</h3>
      <div class="text-sm text-muted mb-6 leading-relaxed">${contentHtml}</div>
      <div class="flex items-center justify-end gap-3">
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
      .replace(/'/g, '&#039;');
  }

  // --- Data Loaders ---
  async function loadManifest() {
    if (state.manifest) return state.manifest;
    const res = await fetch(`data/courses_manifest.json?t=${Date.now()}`, { cache: 'no-store' });
    if (!res.ok) throw new Error(`Không thể nạp manifest: HTTP ${res.status}`);
    state.manifest = await res.json();
    return state.manifest;
  }

  async function loadChapterTheory(courseId, chapterId) {
    const res = await fetch(`data/${courseId}/${chapterId}_theory.md`);
    if (!res.ok) throw new Error(`Không tìm thấy file lý thuyết: ${chapterId}_theory.md`);
    return await res.text();
  }

  async function loadChapterExercises(courseId, chapterId) {
    const res = await fetch(`data/${courseId}/${chapterId}_exercises.json`);
    if (!res.ok) throw new Error(`Không tìm thấy ngân hàng câu hỏi: ${chapterId}_exercises.json`);
    return await res.json();
  }

  async function loadTopic(courseId, topicFile) {
    const res = await fetch(`data/${courseId}/topics/${topicFile}`);
    if (!res.ok) throw new Error(`Không tìm thấy chuyên đề: ${topicFile}`);
    return await res.text();
  }

  // =========================================================================
  // VIEW 1: HOME PORTAL (#/) - Modern Bento Hub
  // =========================================================================
  function renderHomePortal() {
    resetCourseTheme();
    if (readingProgressBar) readingProgressBar.style.width = '0%';

    const manifest = state.manifest;
    const progress = getProgress();

    // 1. Calculate overall stats across all courses
    let totalChaptersAll = 0;
    let completedChaptersAll = 0;
    let totalCorrectQuestionsAll = 0;
    let totalScoreSum = 0;
    let totalCompletedWithScores = 0;

    manifest.courses.forEach((c) => {
      if (c.status === 'active') {
        const cProg = progress[c.id] || {};
        (c.books || []).forEach((b) => {
          (b.chapters || []).forEach((ch) => {
            totalChaptersAll++;
            if (cProg[ch.id] && (cProg[ch.id].attempts || 0) > 0) {
              completedChaptersAll++;
              const best = cProg[ch.id].bestScore || 0;
              const tot = ch.counts ? ch.counts.multiple_choice : 30;
              totalCorrectQuestionsAll += best;
              totalScoreSum += (best / tot) * 10;
              totalCompletedWithScores++;
            }
          });
        });
      }
    });

    const avgScore10 = totalCompletedWithScores > 0
      ? (totalScoreSum / totalCompletedWithScores).toFixed(1)
      : '0.0';

    // 2. Identify Last Studied Chapter for "Học tiếp chương gần nhất" CTA
    let lastChapterInfo = null;
    try {
      const savedLast = localStorage.getItem(STORAGE_LAST_CHAPTER);
      if (savedLast) {
        const parsed = JSON.parse(savedLast);
        const course = manifest.courses.find((c) => c.id === parsed.courseId);
        if (course) {
          for (const b of (course.books || [])) {
            const ch = (b.chapters || []).find((c) => c.id === parsed.chapterId);
            if (ch) {
              lastChapterInfo = { course, chapter: ch };
              break;
            }
          }
        }
      }
    } catch (e) {
      // Ignore
    }

    // 3. Render Bento Course Cards
    const coursesHtml = manifest.courses.map((course) => {
      const isActive = course.status === 'active';
      const cProg = progress[course.id] || {};
      const courseConfig = getCourseUIConfig(course);
      const theme = courseConfig.theme || COURSE_PROFILES.default.theme;

      const totalChapters = (course.books || []).reduce((acc, b) => acc + (b.chapters ? b.chapters.length : 0), 0);
      const completedCount = Object.keys(cProg).filter((cid) => (cProg[cid].attempts || 0) > 0).length;
      const totalQuestions = (course.books || []).reduce((acc, b) => {
        return acc + (b.chapters ? b.chapters.reduce((sum, ch) => sum + (ch.counts ? ch.counts.multiple_choice : 0), 0) : 0);
      }, 0);
      const totalShort = (course.books || []).reduce((acc, b) => {
        return acc + (b.chapters ? b.chapters.reduce((sum, ch) => sum + (ch.counts ? ch.counts.short_answers : 0), 0) : 0);
      }, 0);
      const totalEssay = (course.books || []).reduce((acc, b) => {
        return acc + (b.chapters ? b.chapters.reduce((sum, ch) => sum + (ch.counts ? ch.counts.essays : 0), 0) : 0);
      }, 0);

      const percent = totalChapters > 0 ? Math.round((completedCount / totalChapters) * 100) : 0;
      const radius = 26;
      const circumference = 2 * Math.PI * radius;
      const strokeDashoffset = circumference - (percent / 100) * circumference;

      return `
        <div class="course-card ${!isActive ? 'opacity-70' : ''}" style="--card-accent: linear-gradient(135deg, ${theme.primary} 0%, ${theme.secondary} 100%);">
          <div class="course-card-body">
            <div class="flex items-center justify-between mb-3">
              <div class="flex items-center gap-2">
                <span class="text-2xl">${theme.icon}</span>
                <span class="badge" style="background: ${theme.primary}18; color: ${theme.primary}; border: 1px solid ${theme.primary}40;">${escapeHtml(course.code)}</span>
              </div>
              ${isActive
                ? `<span class="badge badge-success"><span class="w-1.5 h-1.5 rounded-full bg-emerald-500 inline-block mr-1"></span>Sẵn sàng học</span>`
                : `<span class="badge badge-warning">Đang chuẩn bị</span>`}
            </div>

            <h2 class="text-xl font-extrabold mb-2 text-main">${escapeHtml(course.title)}</h2>
            <p class="text-xs text-muted mb-5 leading-relaxed line-clamp-2">${escapeHtml(course.description)}</p>

            ${isActive ? `
              <div class="flex items-center gap-4 bg-slate-50 dark:bg-slate-900/60 p-3.5 rounded-xl border border-subtle mb-4">
                <div class="relative w-14 h-14 flex items-center justify-center flex-shrink-0">
                  <svg class="w-14 h-14 transform -rotate-90">
                    <circle cx="28" cy="28" r="${radius}" stroke="currentColor" stroke-width="4.5" class="text-slate-200 dark:text-slate-800" fill="transparent" />
                    <circle cx="28" cy="28" r="${radius}" stroke="${theme.primary}" stroke-width="4.5" stroke-linecap="round" fill="transparent" stroke-dasharray="${circumference}" stroke-dashoffset="${strokeDashoffset}" style="transition: stroke-dashoffset 0.6s ease;" />
                  </svg>
                  <span class="absolute text-xs font-bold">${percent}%</span>
                </div>
                <div class="flex-1 text-xs">
                  <div class="font-bold text-main mb-0.5">Tiến độ: ${completedCount}/${totalChapters} chương</div>
                  <div class="text-muted">${totalQuestions}+ trắc nghiệm · ${totalShort} câu ngắn</div>
                </div>
              </div>

              <div class="grid grid-cols-3 gap-2 text-center text-xs text-muted mb-2 pt-1 border-t border-subtle">
                <div class="py-1"><strong class="block text-main font-bold">${totalChapters}</strong>Chương</div>
                <div class="py-1"><strong class="block text-main font-bold">${totalQuestions}</strong>Trắc nghiệm</div>
                <div class="py-1"><strong class="block text-main font-bold">${totalEssay}</strong>Tự luận</div>
              </div>
            ` : `
              <div class="py-6 text-center text-xs text-muted italic bg-slate-50 dark:bg-slate-900/40 rounded-xl border border-subtle mb-4">
                Học liệu đang được chuyển đổi sang chuẩn LMS hiện đại.
              </div>
            `}
          </div>

          <div class="course-card-footer">
            ${isActive ? `
              <a href="#/course/${course.id}" class="btn btn-primary w-full" style="background: linear-gradient(135deg, ${theme.primary} 0%, ${theme.secondary} 100%);">
                Vào Ôn Luyện Môn Học →
              </a>
            ` : `
              <button disabled class="btn btn-outline w-full opacity-60 cursor-not-allowed">Chưa mở</button>
            `}
          </div>
        </div>
      `;
    }).join('');

    appEl.innerHTML = `
      <div class="py-2">
        <!-- Hero Section -->
        <div class="bento-hero">
          <div class="max-w-3xl">
            <span class="badge badge-primary mb-3">🎓 Semester Hub LMS · Modern Bento Edition</span>
            <h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight mb-3">
              Cổng Ôn Luyện &amp; Khảo Thí Tương Tác
            </h1>
            <p class="text-muted text-sm sm:text-base leading-relaxed mb-6">
              Nền tảng học thuật chuẩn hóa dành cho sinh viên đại học. Trang bị cơ chế <strong>Sequential Step-by-Step Quiz</strong> tuần tự từng câu, Streak động lực cao, và giải thích chi tiết bám sát 100% giáo trình.
            </p>
          </div>

          <!-- Bento 3-Stat Summary Row -->
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-4">
            <div class="bento-stat-card">
              <div class="bento-stat-icon">📚</div>
              <div>
                <span class="text-xs text-muted font-bold block uppercase tracking-wider">Chương Đã Hoàn Thành</span>
                <span class="text-2xl font-extrabold text-main">${completedChaptersAll} <small class="text-xs text-muted font-normal">/ ${totalChaptersAll || 28} chương</small></span>
              </div>
            </div>

            <div class="bento-stat-card">
              <div class="bento-stat-icon">🎯</div>
              <div>
                <span class="text-xs text-muted font-bold block uppercase tracking-wider">Câu Đúng Chinh Phục</span>
                <span class="text-2xl font-extrabold text-main">${totalCorrectQuestionsAll} <small class="text-xs text-muted font-normal">câu MCQ</small></span>
              </div>
            </div>

            <div class="bento-stat-card">
              <div class="bento-stat-icon">⭐</div>
              <div>
                <span class="text-xs text-muted font-bold block uppercase tracking-wider">Điểm Trung Bình Hệ 10</span>
                <span class="text-2xl font-extrabold text-main">${avgScore10} <small class="text-xs text-muted font-normal">/ 10</small></span>
              </div>
            </div>
          </div>

          <!-- Quick Continue Banner (if available) -->
          ${lastChapterInfo ? `
            <div class="mt-4 p-4 rounded-xl bg-indigo-50/70 dark:bg-indigo-950/40 border border-indigo-200 dark:border-indigo-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
              <div class="flex items-center gap-3">
                <span class="text-2xl">⚡</span>
                <div class="text-xs sm:text-sm">
                  <span class="text-muted">Học tiếp gần nhất:</span>
                  <strong class="text-main ml-1">${escapeHtml(lastChapterInfo.course.title)}</strong> ·
                  <span class="text-indigo-600 dark:text-indigo-400 font-semibold">${escapeHtml(lastChapterInfo.chapter.title)}</span>
                </div>
              </div>
              <a href="#/course/${lastChapterInfo.course.id}/chapter/${lastChapterInfo.chapter.id}" class="btn btn-primary btn-sm whitespace-nowrap">
                Tiếp Tục Học Ngay →
              </a>
            </div>
          ` : ''}
        </div>

        <!-- Course Cards Grid -->
        <div class="mb-4 flex items-center justify-between">
          <h2 class="text-xl font-bold tracking-tight">Danh Sách Môn Học Đang Mở</h2>
          <span class="text-xs text-muted">${manifest.courses.filter(c => c.status === 'active').length} môn sẵn sàng</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          ${coursesHtml}
        </div>
      </div>
    `;
  }

  // =========================================================================
  // VIEW 2: COURSE DASHBOARD (#/course/:course_id)
  // =========================================================================
  function renderCourseDashboard(courseId) {
    const course = state.manifest.courses.find((c) => c.id === courseId);
    if (!course) {
      appEl.innerHTML = `<div class="card text-center py-8"><p class="text-danger-text">Không tìm thấy môn học: ${escapeHtml(courseId)}</p><a href="#/" class="btn btn-primary mt-4">Về trang chủ</a></div>`;
      return;
    }

    applyCourseTheme(course);
    if (readingProgressBar) readingProgressBar.style.width = '0%';

    const progress = getProgress()[courseId] || {};
    const courseConfig = getCourseUIConfig(course);
    const theme = courseConfig.theme || COURSE_PROFILES.default.theme;

    const totalChapters = (course.books || []).reduce((acc, b) => acc + (b.chapters ? b.chapters.length : 0), 0);
    const completedChapters = Object.keys(progress).filter((cid) => (progress[cid].attempts || 0) > 0).length;
    const avgScore = completedChapters > 0
      ? (Object.values(progress).reduce((acc, cur) => acc + (cur.bestScore || 0), 0) / completedChapters).toFixed(1)
      : '0.0';

    const percent = totalChapters > 0 ? Math.round((completedChapters / totalChapters) * 100) : 0;
    const radius = 32;
    const circumference = 2 * Math.PI * radius;
    const strokeDashoffset = circumference - (percent / 100) * circumference;

    // Topics / Chuyên đề tổng hợp Section (if any)
    let topicsHtml = '';
    if (course.topics && course.topics.length > 0) {
      const topicsList = course.topics.map((t) => `
        <div class="card hover:border-indigo-400 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-2">
              <span class="badge badge-primary">Chuyên đề tổng hợp</span>
              <span class="text-xs text-muted font-mono">NotebookLM</span>
            </div>
            <h4 class="text-base font-bold mb-2">${escapeHtml(t.title)}</h4>
            <p class="text-xs text-muted line-clamp-2 mb-4">${escapeHtml(t.summary)}</p>
          </div>
          <a href="#/course/${course.id}/topic/${t.id}" class="btn btn-outline btn-sm w-full">
            📖 Đọc Chuyên Đề →
          </a>
        </div>
      `).join('');

      topicsHtml = `
        <div class="mb-8">
          <h3 class="text-lg font-bold mb-3 flex items-center gap-2">
            <span>📌</span> Chuyên Đề Tổng Hợp &amp; Tinh Hoa Kiến Thức
          </h3>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            ${topicsList}
          </div>
        </div>
      `;
    }

    // Chapters Grouping
    const booksHtml = (course.books || []).map((book) => {
      const chaptersHtml = (book.chapters || []).map((ch) => {
        const chProg = progress[ch.id] || null;
        const isDone = chProg && chProg.attempts > 0;
        const bestScore = isDone ? `${chProg.bestScore}/${ch.counts.multiple_choice}` : 'Chưa làm';

        let rankBadge = 'badge-gray';
        let rankText = 'Chưa làm';
        if (isDone) {
          const pct = Math.round((chProg.bestScore / ch.counts.multiple_choice) * 100);
          if (pct >= 85) { rankBadge = 'badge-success'; rankText = 'Xuất sắc'; }
          else if (pct >= 70) { rankBadge = 'badge-primary'; rankText = 'Giỏi'; }
          else if (pct >= 50) { rankBadge = 'badge-warning'; rankText = 'Khá'; }
          else { rankBadge = 'badge-danger'; rankText = 'Cần ôn lại'; }
        }

        return `
          <div class="card flex flex-col justify-between hover:border-indigo-400">
            <div>
              <div class="flex items-center justify-between mb-2.5">
                <span class="badge" style="background: ${theme.primary}18; color: ${theme.primary}; border: 1px solid ${theme.primary}40;">
                  Chương ${ch.number}
                </span>
                ${isDone
                  ? `<span class="badge ${rankBadge}">🏆 ${bestScore} (${rankText})</span>`
                  : `<span class="badge badge-gray">Chưa làm</span>`}
              </div>
              <h3 class="text-base font-bold mb-2 text-main">${escapeHtml(ch.title)}</h3>
              <p class="text-xs text-muted mb-4 line-clamp-2">${escapeHtml(ch.summary)}</p>
            </div>

            <div class="pt-3 border-t border-subtle">
              <div class="flex items-center justify-between text-xs text-muted mb-3">
                <span>${ch.counts.multiple_choice} MCQ (Tuần tự)</span>
                <span>${ch.counts.short_answers} ngắn · ${ch.counts.essays} tự luận</span>
              </div>
              <a href="#/course/${course.id}/chapter/${ch.id}" class="btn btn-primary btn-sm w-full" style="background: linear-gradient(135deg, ${theme.primary} 0%, ${theme.secondary} 100%);">
                Vào Học Chương →
              </a>
            </div>
          </div>
        `;
      }).join('');

      return `
        <div class="mb-8">
          ${course.books.length > 1 ? `
            <div class="mb-4 pb-2 border-b border-subtle flex items-center justify-between">
              <h3 class="text-lg font-bold text-main">${escapeHtml(book.title)}</h3>
              <span class="text-xs text-muted font-medium">${book.chapters.length} chương</span>
            </div>
          ` : ''}
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            ${chaptersHtml}
          </div>
        </div>
      `;
    }).join('');

    appEl.innerHTML = `
      <div class="py-2">
        <!-- Breadcrumb -->
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="#/">Trang chủ</a>
          <span class="sep">/</span>
          <span class="current">${escapeHtml(course.title)}</span>
        </nav>

        <!-- Bento Course Header Banner -->
        <div class="bento-hero mb-8">
          <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
            <div class="max-w-2xl">
              <div class="flex items-center gap-2 mb-2">
                <span class="text-3xl">${theme.icon}</span>
                <span class="badge" style="background: ${theme.primary}18; color: ${theme.primary}; border: 1px solid ${theme.primary}40;">${escapeHtml(course.code)}</span>
                <span class="badge badge-success">Đang kích hoạt</span>
              </div>
              <h1 class="text-2xl sm:text-3xl font-extrabold mb-2 text-main">${escapeHtml(course.title)}</h1>
              <p class="text-sm text-muted leading-relaxed">${escapeHtml(course.description)}</p>
            </div>

            <!-- Course Progress Gauge -->
            <div class="flex items-center gap-5 bg-white dark:bg-slate-900 p-4 rounded-2xl border border-subtle shadow-sm flex-shrink-0">
              <div class="relative w-20 h-20 flex items-center justify-center">
                <svg class="w-20 h-20 transform -rotate-90">
                  <circle cx="40" cy="40" r="${radius}" stroke="currentColor" stroke-width="6" class="text-slate-200 dark:text-slate-800" fill="transparent" />
                  <circle cx="40" cy="40" r="${radius}" stroke="${theme.primary}" stroke-width="6" stroke-linecap="round" fill="transparent" stroke-dasharray="${circumference}" stroke-dashoffset="${strokeDashoffset}" style="transition: stroke-dashoffset 0.6s ease;" />
                </svg>
                <div class="absolute flex flex-col items-center">
                  <span class="text-base font-extrabold text-main">${percent}%</span>
                  <span class="text-[9px] uppercase tracking-wider text-muted font-bold">Tiến độ</span>
                </div>
              </div>

              <div class="text-xs">
                <div class="font-bold text-main mb-1">Đã học: ${completedChapters}/${totalChapters} chương</div>
                <div class="text-muted mb-1">Điểm TB: <strong>${avgScore}</strong> câu/chương</div>
                <div class="text-[11px] text-subtle">Hệ thống trắc nghiệm tuần tự</div>
              </div>
            </div>
          </div>
        </div>

        ${topicsHtml}

        <!-- Chapters List -->
        <div>
          <div class="mb-4 flex items-center justify-between">
            <h2 class="text-xl font-bold tracking-tight">Ngân Hàng Chương Học Chuẩn Hóa</h2>
            <span class="text-xs text-muted">Tổng cộng ${totalChapters} chương</span>
          </div>
          ${booksHtml}
        </div>
      </div>
    `;
  }

  // =========================================================================
  // VIEW 3: TOPIC VIEWER (#/course/:course_id/topic/:topic_id)
  // =========================================================================
  async function renderTopicViewer(courseId, topicId) {
    const course = state.manifest.courses.find((c) => c.id === courseId);
    if (!course) {
      appEl.innerHTML = `<div class="card text-center py-8"><p class="text-danger-text">Không tìm thấy môn học: ${escapeHtml(courseId)}</p></div>`;
      return;
    }

    applyCourseTheme(course);
    const topic = (course.topics || []).find((t) => t.id === topicId);
    if (!topic) {
      appEl.innerHTML = `<div class="card text-center py-8"><p class="text-danger-text">Không tìm thấy chuyên đề: ${escapeHtml(topicId)}</p><a href="#/course/${courseId}" class="btn btn-primary mt-4">Về môn học</a></div>`;
      return;
    }

    appEl.innerHTML = `<div class="loading"><span class="spinner"></span> Đang tải chuyên đề tổng hợp...</div>`;

    try {
      const mdContent = await loadTopic(courseId, topic.file);
      const html = renderMarkdown(mdContent);

      appEl.innerHTML = `
        <div class="py-2">
          <nav class="breadcrumb" aria-label="Breadcrumb">
            <a href="#/">Trang chủ</a>
            <span class="sep">/</span>
            <a href="#/course/${course.id}">${escapeHtml(course.title)}</a>
            <span class="sep">/</span>
            <span class="current">${escapeHtml(topic.title)}</span>
          </nav>

          <div class="card mb-6">
            <div class="flex items-center justify-between mb-2">
              <span class="badge badge-primary">Chuyên đề tổng hợp</span>
              <a href="#/course/${course.id}" class="text-xs text-muted hover:text-main">← Quay lại môn học</a>
            </div>
            <h1 class="text-2xl font-extrabold mb-2">${escapeHtml(topic.title)}</h1>
            <p class="text-xs text-muted">${escapeHtml(topic.summary)}</p>
          </div>

          <div class="card prose max-w-4xl mx-auto" id="topic-prose">
            ${html}
          </div>
        </div>
      `;

      renderMathAndDiagrams(document.getElementById('topic-prose'));
    } catch (err) {
      appEl.innerHTML = `
        <div class="card text-center py-8">
          <p class="text-danger-text mb-3">Lỗi tải chuyên đề: ${escapeHtml(err.message)}</p>
          <a href="#/course/${courseId}" class="btn btn-primary">Quay lại môn học</a>
        </div>
      `;
    }
  }

  // =========================================================================
  // VIEW 4: CHAPTER WORKSPACE (#/course/:course_id/chapter/:chapter_id)
  // =========================================================================
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

    applyCourseTheme(course);
    recordLastVisited(courseId, chapterId);

    appEl.innerHTML = `<div class="loading"><span class="spinner"></span> Đang nạp dữ liệu chương học &amp; ngân hàng câu hỏi...</div>`;

    try {
      const [theoryMd, exercisesJson] = await Promise.all([
        loadChapterTheory(courseId, chapterId),
        loadChapterExercises(courseId, chapterId)
      ]);

      state.currentCourse = course;
      state.currentChapter = chapterMeta;
      state.theoryMarkdown = theoryMd;
      state.chapterData = exercisesJson;
      state.activeTab = subTab;

      // Reset or initialize Sequential Quiz state for this chapter
      if (!state.quiz.answers || state.quiz.currentChapterId !== chapterId) {
        state.quiz = {
          currentChapterId: chapterId,
          currentIndex: 0,
          maxUnlockedIndex: 0,
          answers: {},
          lockedQuestions: {},
          mode: 'instant',
          streak: 0,
          bestStreak: 0,
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
    const courseConfig = getCourseUIConfig(course);
    const theme = courseConfig.theme || COURSE_PROFILES.default.theme;

    // All chapters in course for quick jump dropdown
    const allChapters = [];
    (course.books || []).forEach((b) => (b.chapters || []).forEach((c) => allChapters.push(c)));

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

        <!-- Chapter Top Header Card -->
        <div class="card mb-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
              <span class="badge mb-1.5" style="background: ${theme.primary}18; color: ${theme.primary}; border: 1px solid ${theme.primary}40;">
                ${escapeHtml(chapter.full_title || `Chương ${chapter.number}`)}
              </span>
              <h1 class="text-xl sm:text-2xl font-extrabold text-main">${escapeHtml(data.chapter_title || chapter.title)}</h1>
            </div>
            <div class="flex items-center gap-2">
              <label for="chapter-select" class="text-xs text-muted whitespace-nowrap font-medium">Chuyển chương:</label>
              <select id="chapter-select" class="card py-1.5 px-3 text-xs font-semibold cursor-pointer">
                ${dropdownOptions}
              </select>
            </div>
          </div>
        </div>

        <!-- 4 Functional Tabs -->
        <div class="tabs-nav" role="tablist">
          <button type="button" class="tab-btn ${state.activeTab === 'theory' ? 'active' : ''}" data-tab="theory" role="tab">
            📖 1. Lý thuyết &amp; Sơ đồ
          </button>
          <button type="button" class="tab-btn ${state.activeTab === 'quiz' ? 'active' : ''}" data-tab="quiz" role="tab">
            ✍️ 2. Trắc nghiệm (${data.multiple_choice.length} câu tuần tự)
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
      if (readingProgressBar) readingProgressBar.style.width = '0%';
      renderTabShort(pane);
    } else if (state.activeTab === 'essay') {
      if (readingProgressBar) readingProgressBar.style.width = '0%';
      renderTabEssay(pane);
    }
  }

  // =========================================================================
  // TAB 1: THEORY (with Sticky TOC & Reading Progress Bar)
  // =========================================================================
  function renderTabTheory(container) {
    const html = renderMarkdown(state.theoryMarkdown);

    container.innerHTML = `
      <div class="theory-layout">
        <!-- Main Theory Text -->
        <div class="card prose" id="theory-prose">
          ${html}
        </div>

        <!-- Sticky Table of Contents (TOC) Sidebar -->
        <aside class="hidden lg:block">
          <div class="theory-toc-card">
            <h4 class="text-xs font-bold uppercase tracking-wider text-muted mb-3 flex items-center gap-1.5">
              <span>📑</span> Mục Lục Chương
            </h4>
            <nav id="theory-toc-nav" class="space-y-0.5"></nav>
          </div>
        </aside>
      </div>
    `;

    const proseEl = document.getElementById('theory-prose');
    renderMathAndDiagrams(proseEl);

    // Build Table of Contents dynamically from headings
    const tocNav = document.getElementById('theory-toc-nav');
    if (tocNav && proseEl) {
      const headings = proseEl.querySelectorAll('h2, h3');
      if (headings.length > 0) {
        headings.forEach((h, idx) => {
          const id = h.id || `toc-heading-${idx}`;
          h.id = id;
          const a = document.createElement('a');
          a.href = `#${id}`;
          a.className = `theory-toc-item ${h.tagName.toLowerCase() === 'h3' ? 'level-3' : ''}`;
          a.textContent = h.textContent.replace(/^#+\s*/, '');
          a.addEventListener('click', (e) => {
            e.preventDefault();
            h.scrollIntoView({ behavior: 'smooth', block: 'start' });
          });
          tocNav.appendChild(a);
        });
      } else {
        tocNav.innerHTML = '<span class="text-xs text-muted italic">Đọc nội dung lý thuyết chi tiết theo các đề mục.</span>';
      }
    }

    // Scroll progress bar handler
    function onScrollProgress() {
      if (state.activeTab !== 'theory' || !readingProgressBar) return;
      const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
      readingProgressBar.style.width = `${Math.min(100, Math.max(0, scrolled))}%`;
    }

    window.removeEventListener('scroll', onScrollProgress);
    window.addEventListener('scroll', onScrollProgress, { passive: true });
    onScrollProgress();
  }

  // =========================================================================
  // TAB 2: SEQUENTIAL STEP-BY-STEP QUIZ ENGINE
  // =========================================================================
  function renderTabQuiz(container) {
    if (readingProgressBar) readingProgressBar.style.width = '0%';

    const questions = state.chapterData.multiple_choice;
    const totalCount = questions.length;
    const answeredCount = Object.keys(state.quiz.answers).length;
    const qIndex = state.quiz.currentIndex;
    const currentQ = questions[qIndex] || questions[0];
    const userChoice = state.quiz.answers[currentQ.id] || null;
    const isLockedCurrent = !!state.quiz.lockedQuestions[currentQ.id];
    const isInstantMode = state.quiz.mode === 'instant';

    const courseConfig = getCourseUIConfig(state.currentCourse);
    const theme = courseConfig.theme || COURSE_PROFILES.default.theme;

    // 1. Build Question Palette (1 .. totalCount)
    const paletteHtml = questions.map((q, idx) => {
      const isCurrent = idx === qIndex;
      const isLocked = idx > state.quiz.maxUnlockedIndex;
      const isAnswered = !!state.quiz.answers[q.id];
      const isCorrect = isAnswered && state.quiz.answers[q.id] === q.correct_answer;
      const isIncorrect = isAnswered && state.quiz.answers[q.id] !== q.correct_answer;

      let classes = 'palette-btn';
      if (isCurrent) classes += ' current';
      if (isLocked) {
        classes += ' locked';
        return `
          <button type="button" class="${classes}" data-idx="${idx}" disabled title="Câu ${idx + 1}: Hoàn thành các câu trước để mở khóa">
            ${idx + 1}
          </button>
        `;
      }

      if (isAnswered) {
        if (isInstantMode) {
          classes += isCorrect ? ' correct' : ' incorrect';
        } else {
          classes += ' answered';
        }
      }

      return `
        <button type="button" class="${classes}" data-idx="${idx}" title="Câu ${idx + 1} (${isAnswered ? 'Đã trả lời' : 'Chưa trả lời'})">
          ${idx + 1}
        </button>
      `;
    }).join('');

    // 2. Build Interactive Options for the focused question
    const letters = ['A', 'B', 'C', 'D'];
    const optionsHtml = letters.map((letter) => {
      const text = currentQ.options[letter] || '';
      const isSelected = userChoice === letter;
      const isRightAnswer = letter === currentQ.correct_answer;

      let optClass = 'quiz-option-card';
      if (isSelected) optClass += ' selected';

      // In instant mode, reveal correct / incorrect styling once answered
      if (isInstantMode && isLockedCurrent) {
        if (isRightAnswer) {
          optClass += ' is-correct';
        } else if (isSelected && !isRightAnswer) {
          optClass += ' is-incorrect';
        } else {
          optClass += ' is-dimmed';
        }
      }

      return `
        <div class="${optClass}" data-letter="${letter}">
          <div class="quiz-option-letter">${letter}</div>
          <div class="quiz-option-text">${escapeHtml(text)}</div>
        </div>
      `;
    }).join('');

    // 3. Explanation Box (Instant mode only, revealed when answered)
    let explanationHtml = '';
    if (isInstantMode && isLockedCurrent) {
      const isCorrect = userChoice === currentQ.correct_answer;
      explanationHtml = `
        <div class="quiz-explanation-box ${isCorrect ? 'correct' : 'incorrect'}">
          <div class="flex items-center gap-2 text-sm font-bold mb-2 ${isCorrect ? 'text-emerald-600 dark:text-emerald-400' : 'text-rose-600 dark:text-rose-400'}">
            <span>${isCorrect ? '✅ Chính xác!' : '❌ Chưa chính xác!'}</span>
            <span>Đáp án đúng: <strong>${currentQ.correct_answer}</strong></span>
          </div>
          <div class="text-xs uppercase font-bold text-muted mb-1">💡 Lời giải &amp; Cơ sở lý thuyết:</div>
          <div class="text-sm prose mb-2">${renderMarkdown(currentQ.explanation)}</div>
          ${currentQ.citation ? `
            <div class="text-xs text-subtle pt-2 border-t border-subtle">
              📖 Căn cứ giáo trình: <em>${escapeHtml(currentQ.citation)}</em>
            </div>
          ` : ''}
        </div>
      `;
    }

    // 4. Navigation Buttons Logic
    const hasNext = qIndex < totalCount - 1;
    const canGoNext = isInstantMode
      ? isLockedCurrent
      : !!userChoice;
    const isLastQuestion = qIndex === totalCount - 1;

    container.innerHTML = `
      <div class="quiz-container">
        <!-- Main Single-Question Focused Stage -->
        <div>
          <div class="quiz-stage-card">
            <!-- Stage Top Bar -->
            <div class="quiz-header-bar">
              <div class="quiz-qnum-badge">
                <span>Câu ${qIndex + 1} / ${totalCount}</span>
                <span class="badge ${currentQ.difficulty === 'hard' ? 'badge-danger' : currentQ.difficulty === 'medium' ? 'badge-warning' : 'badge-primary'}">
                  ${currentQ.difficulty === 'hard' ? 'Vận dụng cao' : currentQ.difficulty === 'medium' ? 'Vận dụng' : 'Nhận biết'}
                </span>
                ${isInstantMode && state.quiz.streak > 1 ? `
                  <span class="quiz-streak-pill" title="Chuỗi trả lời đúng liên tiếp">
                    🔥 Streak: ${state.quiz.streak}
                  </span>
                ` : ''}
              </div>

              <!-- Mode Segmented Selector -->
              <div class="quiz-mode-segmented">
                <button type="button" class="quiz-mode-btn ${isInstantMode ? 'active' : ''}" data-mode="instant" title="Xem giải thích & chấm điểm ngay từng câu">
                  ⚡ Luyện tập tức thì
                </button>
                <button type="button" class="quiz-mode-btn ${!isInstantMode ? 'active' : ''}" data-mode="exam" title="Làm bài thi thử, chấm điểm khi hoàn thành hết">
                  📋 Thi thử
                </button>
              </div>
            </div>

            <!-- Question Stem -->
            <div class="quiz-stem" id="quiz-stem-content">
              ${escapeHtml(currentQ.question)}
            </div>

            <!-- Options Group -->
            <div class="quiz-options">
              ${optionsHtml}
            </div>

            <!-- Explanation Box (Appears after answer in Instant Mode) -->
            ${explanationHtml}

            <!-- Bottom Navigation Bar -->
            <div class="quiz-stage-controls">
              <button type="button" class="btn btn-outline btn-sm" id="btn-quiz-prev" ${qIndex === 0 ? 'disabled' : ''}>
                ← Câu trước
              </button>

              <div class="flex items-center gap-2">
                ${hasNext ? `
                  <button type="button" class="btn btn-primary ${canGoNext ? 'pulse-glow' : 'btn-disabled'}" id="btn-quiz-next" ${canGoNext ? '' : 'disabled'}>
                    Câu tiếp theo →
                  </button>
                ` : `
                  <button type="button" class="btn btn-primary ${canGoNext ? 'pulse-glow' : 'btn-disabled'}" id="btn-quiz-finish" ${canGoNext ? '' : 'disabled'}>
                    🎉 Hoàn Thành &amp; Nộp Bài
                  </button>
                `}
              </div>
            </div>
          </div>
        </div>

        <!-- Sticky Sidebar: Palette, Streak & Progress -->
        <aside>
          <div class="quiz-sidebar-card">
            <div class="flex items-center justify-between mb-2">
              <h3 class="text-sm font-bold text-main">Bảng câu hỏi</h3>
              <span class="text-xs font-mono font-bold" id="palette-count" style="color: ${theme.primary};">${answeredCount}/${totalCount}</span>
            </div>

            <div class="w-full bg-slate-200 dark:bg-slate-700 h-2 rounded-full mb-3 overflow-hidden">
              <div id="palette-progress-bar" class="h-2 rounded-full transition-all duration-300" style="background: ${theme.primary}; width: ${(answeredCount / totalCount) * 100}%"></div>
            </div>

            <div class="text-[11px] text-muted mb-2 flex items-center justify-between">
              <span>Đã hoàn thành ${Math.round((answeredCount / totalCount) * 100)}%</span>
              <span class="text-subtle">Mở khóa tuần tự 🔒</span>
            </div>

            <div class="palette-grid" id="palette-grid-box">
              ${paletteHtml}
            </div>

            <!-- Streak & Session Stats -->
            ${isInstantMode ? `
              <div class="mt-4 pt-3 border-t border-subtle flex items-center justify-between text-xs">
                <span class="text-muted">Chuỗi đúng hiện tại:</span>
                <span class="font-extrabold text-amber-600 dark:text-amber-400">🔥 ${state.quiz.streak} câu</span>
              </div>
              <div class="flex items-center justify-between text-xs text-muted mt-1">
                <span>Kỷ lục streak chương:</span>
                <span class="font-bold text-main">🏆 ${state.quiz.bestStreak} câu</span>
              </div>
            ` : ''}

            <div class="mt-4 pt-3 border-t border-subtle">
              <button type="button" class="btn btn-outline btn-sm w-full text-xs" id="btn-quiz-early-submit">
                Nộp bài &amp; Chấm điểm ngay
              </button>
            </div>
          </div>
        </aside>
      </div>
    `;

    // Render KaTeX for formulas inside current question & explanation
    renderMathAndDiagrams(container);

    // Event Listener: Click Option
    container.querySelectorAll('.quiz-option-card').forEach((card) => {
      card.addEventListener('click', () => {
        if (isInstantMode && isLockedCurrent) return; // Prevent re-answering locked question in instant mode

        const letter = card.getAttribute('data-letter');
        state.quiz.answers[currentQ.id] = letter;

        if (isInstantMode) {
          state.quiz.lockedQuestions[currentQ.id] = true;
          const isCorrect = letter === currentQ.correct_answer;
          if (isCorrect) {
            state.quiz.streak++;
            if (state.quiz.streak > state.quiz.bestStreak) {
              state.quiz.bestStreak = state.quiz.streak;
            }
          } else {
            state.quiz.streak = 0;
          }
          // Unlock next question
          state.quiz.maxUnlockedIndex = Math.max(state.quiz.maxUnlockedIndex, qIndex + 1);
        } else {
          // Exam mode: unlock next question
          state.quiz.maxUnlockedIndex = Math.max(state.quiz.maxUnlockedIndex, qIndex + 1);
        }

        renderTabQuiz(container);
      });
    });

    // Event Listener: Navigation Prev
    const prevBtn = document.getElementById('btn-quiz-prev');
    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        if (state.quiz.currentIndex > 0) {
          state.quiz.currentIndex--;
          renderTabQuiz(container);
        }
      });
    }

    // Event Listener: Navigation Next
    const nextBtn = document.getElementById('btn-quiz-next');
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        if (state.quiz.currentIndex < totalCount - 1 && state.quiz.currentIndex < state.quiz.maxUnlockedIndex) {
          state.quiz.currentIndex++;
          renderTabQuiz(container);
        }
      });
    }

    // Event Listener: Navigation Finish
    const finishBtn = document.getElementById('btn-quiz-finish');
    if (finishBtn) {
      finishBtn.addEventListener('click', () => {
        handleQuizSubmitPrompt();
      });
    }

    // Event Listener: Palette jump
    container.querySelectorAll('.palette-btn:not([disabled])').forEach((btn) => {
      btn.addEventListener('click', () => {
        const idx = parseInt(btn.getAttribute('data-idx'), 10);
        if (!isNaN(idx) && idx <= state.quiz.maxUnlockedIndex) {
          state.quiz.currentIndex = idx;
          renderTabQuiz(container);
        }
      });
    });

    // Event Listener: Mode Switcher
    container.querySelectorAll('.quiz-mode-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        const mode = btn.getAttribute('data-mode');
        if (mode !== state.quiz.mode) {
          state.quiz.mode = mode;
          renderTabQuiz(container);
        }
      });
    });

    // Event Listener: Early Submit
    const earlySubmitBtn = document.getElementById('btn-quiz-early-submit');
    if (earlySubmitBtn) {
      earlySubmitBtn.addEventListener('click', handleQuizSubmitPrompt);
    }
  }

  function handleQuizSubmitPrompt() {
    const questions = state.chapterData.multiple_choice;
    const totalCount = questions.length;
    const answeredCount = Object.keys(state.quiz.answers).length;
    const missing = totalCount - answeredCount;

    if (missing > 0) {
      showDialog(
        'Bạn còn câu hỏi chưa hoàn thành!',
        `<p class="mb-2">Bạn mới trả lời <strong>${answeredCount}/${totalCount}</strong> câu.</p>
         <p class="mb-2">Còn lại <strong>${missing} câu</strong> chưa làm.</p>
         <p>Bạn có chắc chắn muốn nộp bài sớm và chấm điểm các câu đã làm không?</p>`,
        () => performQuizGrading(),
        'Vẫn nộp bài',
        'Làm tiếp'
      );
    } else {
      showDialog(
        'Xác nhận nộp bài & Xem tổng kết',
        `<p>Tuyệt vời! Bạn đã hoàn thành toàn bộ <strong>${totalCount}/${totalCount}</strong> câu hỏi.</p>
         <p>Bấm xác nhận để ghi nhận kết quả và mở bảng phân tích lời giải chi tiết.</p>`,
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

    // Persist result in localStorage
    saveChapterResult(state.currentCourse.id, state.currentChapter.id, score, questions.length);

    renderCurrentTab();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // =========================================================================
  // VIEW 5: QUIZ RESULT & REVIEW DASHBOARD
  // =========================================================================
  function renderQuizResult(container) {
    const questions = state.chapterData.multiple_choice;
    const score = state.quiz.score;
    const total = state.quiz.total;
    const percent = total > 0 ? Math.round((score / total) * 100) : 0;
    const wrongCount = total - score;

    let rankText = 'Cần ôn luyện thêm';
    let rankBadge = 'badge-danger';
    if (percent >= 85) { rankText = 'Xuất sắc'; rankBadge = 'badge-success'; }
    else if (percent >= 70) { rankText = 'Giỏi / Nắm vững'; rankBadge = 'badge-primary'; }
    else if (percent >= 50) { rankText = 'Khá'; rankBadge = 'badge-warning'; }

    const radius = 56;
    const circumference = 2 * Math.PI * radius;
    const strokeDashoffset = circumference - (percent / 100) * circumference;

    const courseConfig = getCourseUIConfig(state.currentCourse);
    const theme = courseConfig.theme || COURSE_PROFILES.default.theme;

    // Filter questions if requested
    const filteredQuestions = state.quiz.filterWrongOnly
      ? questions.filter((q) => state.quiz.answers[q.id] !== q.correct_answer)
      : questions;

    // Render Review Cards
    const reviewCardsHtml = filteredQuestions.map((q) => {
      const originalIdx = questions.findIndex((item) => item.id === q.id);
      const userAns = state.quiz.answers[q.id];
      const isCorrect = userAns === q.correct_answer;

      const letters = ['A', 'B', 'C', 'D'];
      const optionsReview = letters.map((letter) => {
        const text = q.options[letter] || '';
        const isSelected = userAns === letter;
        const isRight = letter === q.correct_answer;

        let badgeStyle = '';
        if (isRight) {
          badgeStyle = 'border-emerald-500 bg-emerald-50/70 dark:bg-emerald-950/30 text-emerald-700 dark:text-emerald-300 font-bold';
        } else if (isSelected && !isRight) {
          badgeStyle = 'border-rose-500 bg-rose-50/70 dark:bg-rose-950/30 text-rose-700 dark:text-rose-300 line-through';
        } else {
          badgeStyle = 'border-subtle bg-surface text-muted';
        }

        return `
          <div class="p-2.5 rounded-lg border text-xs flex items-start gap-2 ${badgeStyle}">
            <strong class="w-5 text-center">${letter}.</strong>
            <span class="flex-1">${escapeHtml(text)}</span>
            ${isRight ? '<span class="text-emerald-600 font-bold">✓ Đáp án đúng</span>' : ''}
            ${isSelected && !isRight ? '<span class="text-rose-600 font-bold">✗ Bạn đã chọn</span>' : ''}
          </div>
        `;
      }).join('');

      return `
        <div class="review-question-card ${isCorrect ? 'was-correct' : 'was-incorrect'}">
          <div class="flex items-center justify-between mb-2">
            <div class="flex items-center gap-2">
              <span class="text-xs font-bold text-main">Câu ${originalIdx + 1}/${total}</span>
              <span class="badge ${isCorrect ? 'badge-success' : 'badge-danger'}">
                ${isCorrect ? '✓ Đúng (+1đ)' : '✗ Chưa đúng (0đ)'}
              </span>
            </div>
            <span class="badge ${q.difficulty === 'hard' ? 'badge-danger' : q.difficulty === 'medium' ? 'badge-warning' : 'badge-primary'}">
              ${q.difficulty === 'hard' ? 'Vận dụng cao' : q.difficulty === 'medium' ? 'Vận dụng' : 'Nhận biết'}
            </span>
          </div>

          <div class="font-bold text-sm text-main mb-3">${escapeHtml(q.question)}</div>
          <div class="space-y-1.5 mb-3">${optionsReview}</div>

          <div class="quiz-explanation-box ${isCorrect ? 'correct' : 'incorrect'}">
            <div class="text-xs uppercase font-bold text-muted mb-1">💡 Lời giải chi tiết:</div>
            <div class="text-xs prose leading-relaxed">${renderMarkdown(q.explanation)}</div>
            ${q.citation ? `
              <div class="text-[11px] text-subtle mt-2 pt-1.5 border-t border-subtle">
                📖 Căn cứ giáo trình: <em>${escapeHtml(q.citation)}</em>
              </div>
            ` : ''}
          </div>
        </div>
      `;
    }).join('');

    container.innerHTML = `
      <div class="max-w-4xl mx-auto py-2">
        <!-- Hero Score Banner -->
        <div class="quiz-result-hero">
          <span class="badge ${rankBadge} mb-3 text-xs uppercase tracking-wider">Xếp loại: ${rankText}</span>

          <div class="result-gauge-wrap">
            <svg class="result-gauge-svg">
              <circle cx="70" cy="70" r="${radius}" class="result-gauge-track" />
              <circle cx="70" cy="70" r="${radius}" class="result-gauge-value" stroke-dasharray="${circumference}" stroke-dashoffset="${strokeDashoffset}" />
            </svg>
            <div class="result-gauge-text">
              <span class="result-gauge-num">${score}<small class="text-xs text-muted font-normal">/${total}</small></span>
              <span class="result-gauge-percent">${percent}%</span>
            </div>
          </div>

          <h2 class="text-2xl font-extrabold text-main mb-2">
            ${percent >= 85 ? '🎉 Xuất sắc! Bạn đã nắm vững chương này!' : percent >= 70 ? '👏 Rất tốt! Đạt chuẩn học thuật kiến thức.' : '💪 Hoàn thành! Hãy ôn lại các câu chưa đúng.'}
          </h2>
          <p class="text-xs text-muted max-w-md mx-auto mb-6">
            Kết quả bài làm đã được lưu an toàn tại trình duyệt. Bạn có thể xem lại chi tiết từng câu hỏi hoặc làm lại bài thi bất cứ lúc nào.
          </p>

          <!-- 4 Stat Badges -->
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 max-w-2xl mx-auto mb-6 text-center">
            <div class="card p-3">
              <span class="text-xs text-muted block">Số câu đúng</span>
              <strong class="text-lg text-emerald-600">${score}</strong>
            </div>
            <div class="card p-3">
              <span class="text-xs text-muted block">Số câu sai</span>
              <strong class="text-lg text-rose-600">${wrongCount}</strong>
            </div>
            <div class="card p-3">
              <span class="text-xs text-muted block">Kỷ lục Streak</span>
              <strong class="text-lg text-amber-600">🔥 ${state.quiz.bestStreak}</strong>
            </div>
            <div class="card p-3">
              <span class="text-xs text-muted block">Chế độ</span>
              <strong class="text-xs text-main">${state.quiz.mode === 'instant' ? 'Luyện tập' : 'Thi thử'}</strong>
            </div>
          </div>

          <!-- Action Buttons -->
          <div class="flex flex-wrap items-center justify-center gap-3">
            <button type="button" class="btn btn-primary btn-sm" id="btn-quiz-retry">
              🔄 Làm Lại Bài Thi (Tuần Tự)
            </button>
            <button type="button" class="btn btn-outline btn-sm" id="btn-quiz-to-theory">
              📖 Đọc Lại Lý Thuyết
            </button>
          </div>
        </div>

        <!-- Review Controls & Filter -->
        <div class="flex items-center justify-between mb-4 flex-wrap gap-2">
          <h3 class="text-lg font-bold text-main">Phân Tích Chi Tiết Từng Câu Hỏi</h3>
          <div class="flex items-center gap-2">
            <button type="button" class="btn btn-sm ${!state.quiz.filterWrongOnly ? 'btn-primary' : 'btn-outline'}" id="btn-filter-all">
              Tất cả (${total})
            </button>
            <button type="button" class="btn btn-sm ${state.quiz.filterWrongOnly ? 'btn-primary' : 'btn-outline'}" id="btn-filter-wrong">
              Chỉ câu sai (${wrongCount})
            </button>
          </div>
        </div>

        <!-- Question Review Cards -->
        <div>
          ${reviewCardsHtml || '<div class="card text-center py-8 text-xs text-muted">Không có câu hỏi nào trong danh mục này.</div>'}
        </div>
      </div>
    `;

    renderMathAndDiagrams(container);

    // Event: Retry
    document.getElementById('btn-quiz-retry').addEventListener('click', () => {
      state.quiz = {
        currentChapterId: state.currentChapter.id,
        currentIndex: 0,
        maxUnlockedIndex: 0,
        answers: {},
        lockedQuestions: {},
        mode: state.quiz.mode || 'instant',
        streak: 0,
        bestStreak: 0,
        submitted: false,
        score: 0,
        total: questions.length,
        filterWrongOnly: false,
        lastSubmittedTime: null
      };
      renderTabQuiz(container);
    });

    // Event: Switch to Theory
    document.getElementById('btn-quiz-to-theory').addEventListener('click', () => {
      switchTab('theory');
    });

    // Event: Filter All
    document.getElementById('btn-filter-all').addEventListener('click', () => {
      state.quiz.filterWrongOnly = false;
      renderQuizResult(container);
    });

    // Event: Filter Wrong
    document.getElementById('btn-filter-wrong').addEventListener('click', () => {
      state.quiz.filterWrongOnly = true;
      renderQuizResult(container);
    });
  }

  // =========================================================================
  // TAB 3: SHORT ANSWER (Pedagogical UI Adaptation)
  // =========================================================================
  function renderTabShort(container) {
    const list = state.chapterData.short_answers;
    const uiConfig = getCourseUIConfig(state.currentCourse);
    const shortCfg = uiConfig.short_answer;
    const theme = uiConfig.theme || COURSE_PROFILES.default.theme;

    const itemsHtml = list.map((item, idx) => {
      return `
        <div class="card mb-6" id="short-item-${item.id}">
          <div class="flex items-center justify-between mb-2">
            <span class="text-sm font-bold" style="color: ${theme.primary};">Câu hỏi ${idx + 1}/${list.length}</span>
            <span class="badge badge-primary">Trả lời ngắn</span>
          </div>
          <div class="font-semibold text-base mb-3 text-main">${escapeHtml(item.question)}</div>

          <div class="mb-3">
            <label for="sa-input-${item.id}" class="block text-xs text-muted mb-1 font-medium">${escapeHtml(shortCfg.label)}</label>
            <textarea id="sa-input-${item.id}" rows="2" class="card w-full text-sm ${shortCfg.isMono ? 'font-mono' : ''} p-3 focus:border-indigo-500" placeholder="${escapeHtml(shortCfg.placeholder)}"></textarea>
          </div>

          <div class="flex items-center justify-between">
            <button type="button" class="btn btn-outline btn-sm btn-check-short" data-sid="${item.id}">
              👁️ Kiểm tra &amp; Đối chiếu đáp án chuẩn
            </button>
          </div>

          <div class="short-answer-box hidden mt-4 p-4 rounded-xl bg-slate-50 dark:bg-slate-900 border border-subtle" id="sa-reveal-${item.id}">
            <div class="text-xs uppercase font-bold text-emerald-600 mb-2">Đáp án chuẩn bám sát giáo trình:</div>
            <div class="text-sm font-medium mb-3 prose">${renderMarkdown(item.expected_answer)}</div>
            ${item.explanation ? `
              <div class="text-xs uppercase font-bold text-muted mb-1">Phân tích &amp; Hướng dẫn:</div>
              <div class="text-xs text-muted prose">${renderMarkdown(item.explanation)}</div>
            ` : ''}
          </div>
        </div>
      `;
    }).join('');

    container.innerHTML = `
      <div class="max-w-4xl mx-auto">
        <div class="card mb-6" style="background: linear-gradient(135deg, ${theme.primary}0d 0%, ${theme.secondary}0d 100%); border-color: ${theme.primary}33;">
          <h2 class="text-base font-bold mb-1" style="color: ${theme.primary};">${escapeHtml(shortCfg.title)}</h2>
          <p class="text-xs text-muted leading-relaxed">
            ${escapeHtml(shortCfg.intro)}
          </p>
        </div>
        ${itemsHtml}
      </div>
    `;

    renderMathAndDiagrams(container);

    // Toggle reveal listeners
    container.querySelectorAll('.btn-check-short').forEach((btn) => {
      btn.addEventListener('click', () => {
        const sid = btn.getAttribute('data-sid');
        const box = document.getElementById(`sa-reveal-${sid}`);
        if (box) {
          box.classList.toggle('hidden');
          btn.textContent = box.classList.contains('hidden')
            ? '👁️ Kiểm tra & Đối chiếu đáp án chuẩn'
            : 'Ẩn đáp án chuẩn';
          renderMathAndDiagrams(box);
        }
      });
    });
  }

  // =========================================================================
  // TAB 4: ESSAY & PROBLEM SOLVING (Pedagogical UI Adaptation)
  // =========================================================================
  function renderTabEssay(container) {
    const list = state.chapterData.essays;
    const uiConfig = getCourseUIConfig(state.currentCourse);
    const essayCfg = uiConfig.essay;
    const theme = uiConfig.theme || COURSE_PROFILES.default.theme;

    const itemsHtml = list.map((item, idx) => {
      const stepsHtml = (item.solution_steps || []).map((step) => {
        return `<div class="mb-3 pl-3.5 border-l-2" style="border-color: ${theme.primary};">${renderMarkdown(step)}</div>`;
      }).join('');

      return `
        <div class="card mb-6" id="essay-item-${item.id}">
          <div class="flex items-center justify-between mb-2">
            <span class="text-sm font-bold" style="color: ${theme.primary};">Bài toán ${idx + 1}/${list.length}</span>
            <span class="badge badge-primary">${escapeHtml(essayCfg.badge)}</span>
          </div>
          <h3 class="text-lg font-bold mb-2 text-main">${escapeHtml(item.title)}</h3>
          <div class="text-sm text-main mb-4 prose">${renderMarkdown(item.problem)}</div>

          <div>
            <button type="button" class="btn btn-outline btn-sm btn-toggle-essay" data-eid="${item.id}">
              🔍 Xem Lời Giải Từng Bước (Step-by-step Solution)
            </button>
          </div>

          <div class="essay-solution hidden mt-4 p-4 rounded-xl bg-slate-50 dark:bg-slate-900 border border-subtle" id="essay-sol-${item.id}">
            <div class="text-xs uppercase font-bold mb-3" style="color: ${theme.primary};">Lời giải chi tiết từng bước:</div>
            <div class="text-sm prose">
              ${stepsHtml}
            </div>
          </div>
        </div>
      `;
    }).join('');

    container.innerHTML = `
      <div class="max-w-4xl mx-auto">
        <div class="card mb-6" style="background: linear-gradient(135deg, ${theme.primary}0d 0%, ${theme.secondary}0d 100%); border-color: ${theme.primary}33;">
          <h2 class="text-base font-bold mb-1" style="color: ${theme.primary};">${escapeHtml(essayCfg.title)}</h2>
          <p class="text-xs text-muted leading-relaxed">
            ${escapeHtml(essayCfg.intro)}
          </p>
        </div>
        ${itemsHtml}
      </div>
    `;

    renderMathAndDiagrams(container);

    // Toggle solution listeners
    container.querySelectorAll('.btn-toggle-essay').forEach((btn) => {
      btn.addEventListener('click', () => {
        const eid = btn.getAttribute('data-eid');
        const sol = document.getElementById(`essay-sol-${eid}`);
        if (sol) {
          sol.classList.toggle('hidden');
          btn.textContent = sol.classList.contains('hidden')
            ? '🔍 Xem Lời Giải Từng Bước (Step-by-step Solution)'
            : 'Ẩn lời giải chi tiết';
          renderMathAndDiagrams(sol);
        }
      });
    });
  }

  // =========================================================================
  // HASH ROUTER
  // =========================================================================
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

    // Route: #/course/:course_id/chapter/:chapter_id (optional subTab)
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

  // --- Bootstrap Application ---
  window.addEventListener('hashchange', handleRouting);
  window.addEventListener('DOMContentLoaded', () => {
    initTheme();
    handleRouting();
  });

})();
