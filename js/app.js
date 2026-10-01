/**
 * ====================================================================
 * SEMESTER HUB - JAVASCRIPT APPLICATION LOGIC
 * ====================================================================
 * Quản lý trạng thái, hiển thị học phần, thời khóa biểu, tính toán deadline và tương tác
 */

(function () {
  'use strict';

  // State Management
  let semesterData = null;
  let activeTab = 'courses'; // 'courses', 'tasks', 'timetable', 'syllabus', 'resources'
  let taskFilter = 'all'; // 'all', 'overdue', 'today', 'upcoming', 'done'
  let taskCourseFilter = 'all';
  let taskSortBy = 'deadline'; // 'deadline', 'priority', 'course', 'title'
  let taskViewMode = 'by-course'; // 'by-course', 'kanban'
  let searchQuery = '';
  let activeCourse = null;
  let activeChapter = null;
  let activeChapterTab = 'content';
  let activeCourseTaskId = null;

  // LocalStorage Keys
  const LS_TASKS_STATUS = 'semester_tasks_status_v1';
  const LS_CUSTOM_TASKS = 'semester_custom_tasks_v1';
  const LS_THEME = 'semester_theme';

  // Color mapping for tailwind
  const COLOR_MAP = {
    indigo: {
      bg: 'bg-indigo-50 dark:bg-indigo-950/40',
      border: 'border-indigo-200 dark:border-indigo-800',
      text: 'text-indigo-600 dark:text-indigo-400',
      badge: 'bg-indigo-100 text-indigo-700 dark:bg-indigo-900/60 dark:text-indigo-300',
      accent: '#6366f1',
      ring: 'focus:ring-indigo-500'
    },
    emerald: {
      bg: 'bg-emerald-50 dark:bg-emerald-950/40',
      border: 'border-emerald-200 dark:border-emerald-800',
      text: 'text-emerald-600 dark:text-emerald-400',
      badge: 'bg-emerald-100 text-emerald-700 dark:bg-emerald-900/60 dark:text-emerald-300',
      accent: '#10b981',
      ring: 'focus:ring-emerald-500'
    },
    rose: {
      bg: 'bg-rose-50 dark:bg-rose-950/40',
      border: 'border-rose-200 dark:border-rose-800',
      text: 'text-rose-600 dark:text-rose-400',
      badge: 'bg-rose-100 text-rose-700 dark:bg-rose-900/60 dark:text-rose-300',
      accent: '#f43f5e',
      ring: 'focus:ring-rose-500'
    },
    sky: {
      bg: 'bg-sky-50 dark:bg-sky-950/40',
      border: 'border-sky-200 dark:border-sky-800',
      text: 'text-sky-600 dark:text-sky-400',
      badge: 'bg-sky-100 text-sky-700 dark:bg-sky-900/60 dark:text-sky-300',
      accent: '#0284c7',
      ring: 'focus:ring-sky-500'
    },
    purple: {
      bg: 'bg-purple-50 dark:bg-purple-950/40',
      border: 'border-purple-200 dark:border-purple-800',
      text: 'text-purple-600 dark:text-purple-400',
      badge: 'bg-purple-100 text-purple-700 dark:bg-purple-900/60 dark:text-purple-300',
      accent: '#a855f7',
      ring: 'focus:ring-purple-500'
    },
    amber: {
      bg: 'bg-amber-50 dark:bg-amber-950/40',
      border: 'border-amber-200 dark:border-amber-800',
      text: 'text-amber-600 dark:text-amber-400',
      badge: 'bg-amber-100 text-amber-700 dark:bg-amber-900/60 dark:text-amber-300',
      accent: '#f59e0b',
      ring: 'focus:ring-amber-500'
    }
  };

  /**
   * Helper: Initialize Data & merge LocalStorage state
   */
  function initData() {
    if (!window.SEMESTER_DATA) {
      console.error('Không tìm thấy dữ liệu window.SEMESTER_DATA từ data/courses.js');
      return;
    }

    // Clone data to avoid direct mutation of global object
    semesterData = JSON.parse(JSON.stringify(window.SEMESTER_DATA));
    semesterData.courses.forEach(course => {
      course.chapters = course.chapters || [];
      course.chapters.forEach(chapter => {
        chapter.tasks = chapter.tasks || [];
      });
    });

    // Merge custom tasks added via web UI
    const customTasks = getStoredCustomTasks();
    if (Array.isArray(customTasks)) {
      customTasks.forEach(ct => {
        const targetCourse = semesterData.courses.find(c => c.id === ct.courseId);
        if (targetCourse) {
          const targetChapter = targetCourse.chapters.find(chapter => chapter.id === ct.chapterId) ||
            targetCourse.chapters[0] || ensureUncategorizedChapter(targetCourse);
          ct.chapterId = targetChapter.id;
          // Avoid duplicate task ID
          if (!targetChapter.tasks.some(task => task.id === ct.id)) {
            targetChapter.tasks.push(ct);
          }
        }
      });
    }

    // Merge status from localStorage if present
    const savedTaskStatuses = getStoredTaskStatuses();
    semesterData.courses.forEach(course => {
      course.chapters.forEach(chapter => {
        chapter.tasks.forEach(task => {
          if (savedTaskStatuses[task.id] !== undefined) {
            task.status = savedTaskStatuses[task.id];
          }
        });
      });
    });
  }

  function ensureUncategorizedChapter(course) {
    let chapter = course.chapters.find(item => item.id === 'uncategorized');
    if (!chapter) {
      chapter = { id: 'uncategorized', title: 'Chưa phân chương', content: '', tasks: [] };
      course.chapters.push(chapter);
    }
    return chapter;
  }

  function getAllTasks() {
    const tasks = [];
    semesterData.courses.forEach(course => {
      course.chapters.forEach(chapter => {
        chapter.tasks.forEach(task => {
          tasks.push({
            ...task,
            courseId: course.id,
            courseName: course.name,
            courseCode: course.code || course.name,
            badgeColor: course.badgeColor,
            chapterId: chapter.id,
            chapterTitle: chapter.title
          });
        });
      });
    });
    return tasks;
  }

  function getStoredTaskStatuses() {
    try {
      const data = localStorage.getItem(LS_TASKS_STATUS);
      return data ? JSON.parse(data) : {};
    } catch (e) {
      return {};
    }
  }

  function getStoredCustomTasks() {
    try {
      const data = localStorage.getItem(LS_CUSTOM_TASKS);
      return data ? JSON.parse(data) : [];
    } catch (e) {
      return [];
    }
  }

  function saveTaskStatus(taskId, newStatus) {
    const statuses = getStoredTaskStatuses();
    statuses[taskId] = newStatus;
    localStorage.setItem(LS_TASKS_STATUS, JSON.stringify(statuses));

    // Update in-memory state
    semesterData.courses.forEach(course => {
      course.chapters.forEach(chapter => {
        const task = chapter.tasks.find(item => item.id === taskId);
        if (task) task.status = newStatus;
      });
    });

    renderStats();
    if (activeTab === 'tasks') renderTasksTab();
    if (activeTab === 'courses') renderCoursesTab();
    if (activeChapter && activeChapterTab === 'tasks') updateChapterTasks();
    if (activeCourseTaskId) renderCourseTaskDetail();
  }

  /**
   * Deadline calculations
   */
  function getDeadlineInfo(deadlineStr, status) {
    if (status === 'done') {
      return {
        label: 'Đã hoàn thành',
        type: 'done',
        badgeClass: 'bg-emerald-100 text-emerald-700 dark:bg-emerald-900/50 dark:text-emerald-300',
        daysDiff: 0
      };
    }

    if (!deadlineStr) {
      return {
        label: 'Không có hạn',
        type: 'none',
        badgeClass: 'bg-slate-100 text-slate-600 dark:bg-slate-800 dark:text-slate-400',
        daysDiff: 999
      };
    }

    const today = new Date();
    today.setHours(0, 0, 0, 0);

    const deadline = new Date(deadlineStr);
    deadline.setHours(0, 0, 0, 0);

    const diffTime = deadline.getTime() - today.getTime();
    const diffDays = Math.round(diffTime / (1000 * 60 * 60 * 24));

    if (diffDays < 0) {
      const absDays = Math.abs(diffDays);
      return {
        label: `Quá hạn ${absDays} ngày`,
        type: 'overdue',
        badgeClass: 'bg-rose-100 text-rose-700 dark:bg-rose-900/60 dark:text-rose-300 font-semibold',
        daysDiff: diffDays
      };
    } else if (diffDays === 0) {
      return {
        label: 'Hạn chót hôm nay!',
        type: 'today',
        badgeClass: 'bg-amber-100 text-amber-800 dark:bg-amber-900/60 dark:text-amber-200 font-bold animate-pulse',
        daysDiff: 0
      };
    } else if (diffDays === 1) {
      return {
        label: 'Còn 1 ngày',
        type: 'urgent',
        badgeClass: 'bg-amber-100 text-amber-700 dark:bg-amber-900/50 dark:text-amber-300 font-medium',
        daysDiff: 1
      };
    } else if (diffDays <= 7) {
      return {
        label: `Còn ${diffDays} ngày`,
        type: 'upcoming',
        badgeClass: 'bg-blue-100 text-blue-700 dark:bg-blue-900/50 dark:text-blue-300 font-medium',
        daysDiff: diffDays
      };
    } else {
      return {
        label: `Còn ${diffDays} ngày`,
        type: 'normal',
        badgeClass: 'bg-slate-100 text-slate-700 dark:bg-slate-800 dark:text-slate-300',
        daysDiff: diffDays
      };
    }
  }

  /**
   * Compute stats for KPI cards
   */
  function renderStats() {
    if (!semesterData) return;

    let totalCourses = semesterData.courses.length;
    const allTasks = getAllTasks();

    let completedTasks = allTasks.filter(t => t.status === 'done').length;
    let totalTasks = allTasks.length;
    let progressPercent = totalTasks > 0 ? Math.round((completedTasks / totalTasks) * 100) : 0;

    let urgentTasks = allTasks.filter(t => {
      if (t.status === 'done') return false;
      const info = getDeadlineInfo(t.deadline, t.status);
      return info.type === 'overdue' || info.type === 'today' || (info.type === 'urgent' && info.daysDiff <= 3);
    });

    // Update UI elements
    const elTotalCourses = document.getElementById('stat-total-courses');
    const elTotalTasks = document.getElementById('stat-total-tasks');
    const elUrgentTasks = document.getElementById('stat-urgent-tasks');
    const elTaskProgress = document.getElementById('stat-task-progress');
    const elProgressBar = document.getElementById('stat-progress-bar');
    const elSemesterTitle = document.getElementById('header-semester-title');
    const elStudentInfo = document.getElementById('header-student-info');
    const elAnnouncement = document.getElementById('announcement-banner');
    const elAnnouncementText = document.getElementById('announcement-text');

    if (elTotalCourses) elTotalCourses.textContent = totalCourses;
    if (elTotalTasks) elTotalTasks.textContent = totalTasks;
    if (elUrgentTasks) elUrgentTasks.textContent = urgentTasks.length;
    if (elTaskProgress) elTaskProgress.textContent = `${completedTasks}/${totalTasks} (${progressPercent}%)`;
    if (elProgressBar) elProgressBar.style.width = `${progressPercent}%`;

    if (elSemesterTitle) elSemesterTitle.textContent = semesterData.semesterInfo.title;
    if (elStudentInfo) {
      elStudentInfo.textContent = `${semesterData.semesterInfo.studentName} • ${semesterData.semesterInfo.major} • Mục tiêu GPA: ${semesterData.semesterInfo.targetGPA}`;
    }

    if (semesterData.semesterInfo.announcement && elAnnouncement) {
      elAnnouncement.classList.remove('hidden');
      if (elAnnouncementText) elAnnouncementText.textContent = semesterData.semesterInfo.announcement;
    }
  }

  /**
   * TAB 1: RENDER COURSES
   */
  function renderCoursesTab() {
    const container = document.getElementById('courses-grid');
    if (!container || !semesterData) return;

    let filtered = semesterData.courses;
    if (searchQuery.trim()) {
      const q = searchQuery.toLowerCase();
      filtered = filtered.filter(c =>
        (c.name || '').toLowerCase().includes(q) ||
        (c.code || '').toLowerCase().includes(q) ||
        (c.content || '').toLowerCase().includes(q)
      );
    }

    if (filtered.length === 0) {
      container.innerHTML = `
        <div class="col-span-full py-12 text-center text-slate-500 dark:text-slate-400">
          <i data-lucide="search-x" class="w-12 h-12 mx-auto mb-3 opacity-40"></i>
          <p class="text-base font-medium">Không tìm thấy học phần nào khớp với từ khóa "${searchQuery}".</p>
        </div>
      `;
      lucide.createIcons();
      return;
    }

    container.innerHTML = filtered.map(course => {
      const colorScheme = COLOR_MAP[course.badgeColor] || COLOR_MAP.indigo;

      // Pending tasks
      const courseTasks = course.chapters.flatMap(chapter => chapter.tasks);
      const activeTasksCount = courseTasks.filter(task => task.status !== 'done').length;
      const contentPreview = course.chapters[0]?.title || 'Chưa có chương';

      return `
        <article onclick="window.SemesterApp.openCourseDetail('${course.id}')"
           onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();window.SemesterApp.openCourseDetail('${course.id}')}"
           role="button" tabindex="0"
           class="flex flex-col cursor-pointer rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-6 shadow-sm hover:shadow-md hover:border-indigo-300 dark:hover:border-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition-all duration-200">
          <!-- Card Header -->
          <div class="flex items-start justify-between gap-3 mb-4">
            <div>
              <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold ${colorScheme.badge} mb-1.5">
                Học phần
              </span>
              <h3 class="text-lg font-bold text-slate-900 dark:text-white line-clamp-1 leading-snug">
                ${course.name}
              </h3>
            </div>
          </div>

          <p class="text-sm text-slate-600 dark:text-slate-400 line-clamp-3 mb-4 leading-relaxed">
            ${contentPreview}
          </p>

          <div class="mt-auto pt-3 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between text-xs">
            <span class="inline-flex items-center gap-1 font-medium ${activeTasksCount > 0 ? 'text-amber-600 dark:text-amber-400' : 'text-slate-400'}">
              <i data-lucide="check-square" class="w-4 h-4"></i>
              ${activeTasksCount > 0 ? `${activeTasksCount} task cần làm` : 'Không có task tồn'}
            </span>
            <span class="font-semibold text-indigo-600 dark:text-indigo-400 inline-flex items-center gap-1">
              Mở học phần
              <i data-lucide="chevron-right" class="w-4 h-4"></i>
            </span>
          </div>
        </article>
      `;
    }).join('');

    lucide.createIcons();
  }

  function getLinkIcon(type) {
    type = (type || '').toLowerCase();
    if (type.includes('classroom')) return 'layout-grid';
    if (type.includes('drive')) return 'hard-drive';
    if (type.includes('github') || type.includes('repo')) return 'github';
    if (type.includes('trello') || type.includes('jira')) return 'kanban';
    if (type.includes('kaggle')) return 'database';
    return 'link';
  }

  /**
   * TAB 2: RENDER TASKS & DEADLINES
   */
  function renderTasksTab() {
    const listContainer = document.getElementById('tasks-container');
    const kanbanContainer = document.getElementById('tasks-kanban');
    const courseSelect = document.getElementById('task-course-filter');
    if (!semesterData) return;

    // Populate course filter dropdown if needed
    if (courseSelect && courseSelect.options.length <= 1) {
      courseSelect.innerHTML = '<option value="all">Tất cả môn học</option>';
      semesterData.courses.forEach(c => {
        const opt = document.createElement('option');
        opt.value = c.id;
        opt.textContent = c.name;
        courseSelect.appendChild(opt);
      });
      courseSelect.value = taskCourseFilter;
    }

    let tasks = getAllTasks();

    // Filter by Course
    if (taskCourseFilter !== 'all') {
      tasks = tasks.filter(t => t.courseId === taskCourseFilter);
    }

    // Filter by Search Query
    if (searchQuery.trim()) {
      const q = searchQuery.toLowerCase();
      tasks = tasks.filter(t =>
        t.title.toLowerCase().includes(q) ||
        t.courseName.toLowerCase().includes(q) ||
        t.courseCode.toLowerCase().includes(q) ||
        (t.note && t.note.toLowerCase().includes(q))
      );
    }

    // Filter by Status / Deadline
    tasks = tasks.filter(t => {
      const info = getDeadlineInfo(t.deadline, t.status);
      if (taskFilter === 'all') return true;
      if (taskFilter === 'done') return t.status === 'done';
      if (taskFilter === 'overdue') return t.status !== 'done' && info.type === 'overdue';
      if (taskFilter === 'today') return t.status !== 'done' && info.type === 'today';
      if (taskFilter === 'upcoming') return t.status !== 'done' && info.daysDiff <= 7 && info.daysDiff >= 0;
      return true;
    });

    // Sort tasks
    tasks.sort((a, b) => {
      if (taskSortBy === 'deadline') {
        if (a.status === 'done' && b.status !== 'done') return 1;
        if (a.status !== 'done' && b.status === 'done') return -1;
        return (a.deadline || '9999').localeCompare(b.deadline || '9999');
      } else if (taskSortBy === 'priority') {
        const pMap = { high: 3, medium: 2, low: 1 };
        return (pMap[b.priority] || 0) - (pMap[a.priority] || 0);
      } else if (taskSortBy === 'course') {
        return a.courseCode.localeCompare(b.courseCode);
      } else if (taskSortBy === 'title') {
        return a.title.localeCompare(b.title);
      }
      return 0;
    });

    // Toggle View modes
    if (taskViewMode === 'kanban') {
      if (listContainer) listContainer.classList.add('hidden');
      if (kanbanContainer) {
        kanbanContainer.classList.remove('hidden');
        renderKanbanView(tasks);
      }
    } else {
      if (kanbanContainer) kanbanContainer.classList.add('hidden');
      if (listContainer) {
        listContainer.classList.remove('hidden');
        renderGroupedListView(tasks);
      }
    }

    lucide.createIcons();
  }

  function changeTaskSort(sortBy) {
    taskSortBy = sortBy;
    renderTasksTab();
  }

  function renderGroupedListView(tasks) {
    const container = document.getElementById('tasks-container');
    if (!container) return;

    if (tasks.length === 0) {
      container.innerHTML = `
        <div class="py-16 text-center text-slate-500 dark:text-slate-400">
          <i data-lucide="check-circle" class="w-12 h-12 mx-auto mb-3 opacity-40 text-emerald-500"></i>
          <p class="text-base font-medium">Không có công việc nào thỏa mãn bộ lọc hiện tại.</p>
          <p class="text-xs text-slate-400 mt-1">Tuyệt vời! Bạn đã hoàn thành hết hoặc chưa có task mới.</p>
        </div>
      `;
      return;
    }

    // Group tasks by course
    const groups = {};
    tasks.forEach(t => {
      if (!groups[t.courseId]) {
        groups[t.courseId] = {
          courseName: t.courseName,
          courseCode: t.courseCode,
          badgeColor: t.badgeColor,
          items: []
        };
      }
      groups[t.courseId].items.push(t);
    });

    container.innerHTML = Object.keys(groups).map(courseId => {
      const g = groups[courseId];
      const colorScheme = COLOR_MAP[g.badgeColor] || COLOR_MAP.indigo;

      const itemsHtml = g.items.map(task => renderTaskCard(task)).join('');

      return `
        <div class="mb-8 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-5 shadow-sm">
          <div class="flex items-center justify-between pb-3 mb-4 border-b border-slate-100 dark:border-slate-800">
            <div class="flex items-center gap-2.5">
              <span class="w-2.5 h-2.5 rounded-full" style="background-color: ${colorScheme.accent};"></span>
              <h3 class="font-bold text-slate-900 dark:text-white text-base">
                ${g.courseCode} • ${g.courseName}
              </h3>
            </div>
            <span class="text-xs font-medium text-slate-500 dark:text-slate-400 bg-slate-100 dark:bg-slate-800 px-2.5 py-1 rounded-full">
              ${g.items.length} task
            </span>
          </div>
          <div class="space-y-3">
            ${itemsHtml}
          </div>
        </div>
      `;
    }).join('');
  }

  function renderKanbanView(tasks) {
    const colTodo = document.getElementById('kanban-col-todo');
    const colInProgress = document.getElementById('kanban-col-inprogress');
    const colDone = document.getElementById('kanban-col-done');

    const countTodo = document.getElementById('kanban-count-todo');
    const countInProgress = document.getElementById('kanban-count-inprogress');
    const countDone = document.getElementById('kanban-count-done');

    const todos = tasks.filter(t => t.status === 'todo');
    const inProgress = tasks.filter(t => t.status === 'in-progress');
    const dones = tasks.filter(t => t.status === 'done');

    if (countTodo) countTodo.textContent = todos.length;
    if (countInProgress) countInProgress.textContent = inProgress.length;
    if (countDone) countDone.textContent = dones.length;

    if (colTodo) {
      colTodo.innerHTML = todos.length ? todos.map(t => renderTaskCard(t, true)).join('') : '<p class="text-xs text-slate-400 text-center py-6">Trống</p>';
    }
    if (colInProgress) {
      colInProgress.innerHTML = inProgress.length ? inProgress.map(t => renderTaskCard(t, true)).join('') : '<p class="text-xs text-slate-400 text-center py-6">Trống</p>';
    }
    if (colDone) {
      colDone.innerHTML = dones.length ? dones.map(t => renderTaskCard(t, true)).join('') : '<p class="text-xs text-slate-400 text-center py-6">Trống</p>';
    }
  }

  function renderTaskCard(task, isCompact = false) {
    const deadlineInfo = getDeadlineInfo(task.deadline, task.status);
    const isDone = task.status === 'done';

    // Priority badge
    let priorityBadge = '';
    if (task.priority === 'high') {
      priorityBadge = '<span class="inline-flex items-center gap-1 text-[11px] font-semibold text-rose-600 dark:text-rose-400"><i data-lucide="flame" class="w-3.5 h-3.5"></i>Ưu tiên cao</span>';
    } else if (task.priority === 'medium') {
      priorityBadge = '<span class="inline-flex items-center gap-1 text-[11px] font-medium text-amber-600 dark:text-amber-400">Trung bình</span>';
    } else {
      priorityBadge = '<span class="inline-flex items-center gap-1 text-[11px] font-normal text-slate-400">Thấp</span>';
    }

    return `
      <div class="task-item group relative rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-800/40 p-4 transition-all hover:bg-white dark:hover:bg-slate-800 hover:shadow-sm ${isDone ? 'opacity-70' : ''}">
        <div class="flex items-start gap-3.5">
          <!-- Checkbox -->
          <div class="pt-0.5 shrink-0">
            <input type="checkbox" id="chk-${task.id}" 
                   class="task-checkbox w-5 h-5 rounded-md border-slate-300 dark:border-slate-600 text-indigo-600 focus:ring-indigo-500 cursor-pointer"
                   ${isDone ? 'checked' : ''}
                   onchange="window.SemesterApp.toggleTask('${task.id}', this.checked)">
          </div>

          <!-- Content -->
          <div class="flex-1 min-w-0">
            <div class="flex flex-wrap items-center gap-2 mb-1.5">
              ${isCompact ? `<span class="text-[11px] font-semibold text-indigo-600 dark:text-indigo-400 bg-indigo-50 dark:bg-indigo-950/60 px-2 py-0.5 rounded">${task.courseCode}</span>` : ''}
              <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[11px] ${deadlineInfo.badgeClass}">
                <i data-lucide="clock" class="w-3 h-3"></i>
                ${deadlineInfo.label}
              </span>
              ${priorityBadge}
            </div>

            <label for="chk-${task.id}" class="cursor-pointer block">
              <h4 class="task-title font-semibold text-sm text-slate-900 dark:text-slate-100 leading-snug ${isDone ? 'line-through text-slate-400 dark:text-slate-500' : ''}">
                ${task.title}
              </h4>
            </label>

            ${task.note ? `
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-1.5 leading-relaxed bg-slate-100/60 dark:bg-slate-800/80 p-2 rounded-lg border border-slate-200/50 dark:border-slate-700/50">
                ${task.note}
              </p>
            ` : ''}

            <!-- Task Meta & Status Switcher -->
            <div class="mt-3 flex items-center justify-between text-xs text-slate-500 dark:text-slate-400">
              <div class="flex items-center gap-2">
                <i data-lucide="calendar" class="w-3.5 h-3.5"></i>
                <span>Hạn chót: <strong>${task.deadline || 'Chưa đặt'}</strong></span>
              </div>

              <!-- Quick Status Selector -->
              <select onchange="window.SemesterApp.updateTaskStatus('${task.id}', this.value)"
                      class="text-xs rounded-lg border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 py-1 px-2 focus:ring-1 focus:ring-indigo-500 cursor-pointer">
                <option value="todo" ${task.status === 'todo' ? 'selected' : ''}>Cần làm</option>
                <option value="in-progress" ${task.status === 'in-progress' ? 'selected' : ''}>Đang làm</option>
                <option value="done" ${task.status === 'done' ? 'selected' : ''}>Đã xong</option>
              </select>
            </div>
          </div>
        </div>
      </div>
    `;
  }

  /**
   * TAB 3: RENDER TIMETABLE (THỜI KHÓA BIỂU TUẦN)
   */
  function renderTimetableTab() {
    const container = document.getElementById('timetable-container');
    if (!container || !semesterData) return;

    // Get current day of week (Sunday is 0, Monday is 1 -> in VN Monday is 2, Tuesday is 3...)
    const now = new Date();
    const jsDay = now.getDay();
    const currentVnDay = jsDay === 0 ? 8 : jsDay + 1; // 2..7, 8 for Sunday

    const days = [
      { id: 2, name: 'Thứ Hai', short: 'T2' },
      { id: 3, name: 'Thứ Ba', short: 'T3' },
      { id: 4, name: 'Thứ Tư', short: 'T4' },
      { id: 5, name: 'Thứ Năm', short: 'T5' },
      { id: 6, name: 'Thứ Sáu', short: 'T6' },
      { id: 7, name: 'Thứ Bảy', short: 'T7' }
    ];

    const dayColumnsHtml = days.map(d => {
      const isToday = d.id === currentVnDay;

      // Find courses scheduled on this day
      const scheduledCourses = semesterData.courses.filter(c => {
        if (c.timetable && c.timetable.day === d.id) return true;
        // Fallback: check if schedule string mentions "Thứ d.id"
        return (c.schedule || '').toLowerCase().includes(`thứ ${d.id}`);
      });

      const coursesCardsHtml = scheduledCourses.length > 0 ? scheduledCourses.map(course => {
        const colorScheme = COLOR_MAP[course.badgeColor] || COLOR_MAP.indigo;
        const tt = course.timetable || {};

        return `
          <div class="rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-4 shadow-sm hover:shadow transition-all group">
            <div class="flex items-start justify-between gap-2 mb-2">
              <span class="text-[11px] font-bold ${colorScheme.badge} px-2 py-0.5 rounded">
                ${course.code || course.name}
              </span>
              <button onclick="window.SemesterApp.openCourseDetail('${course.id}')"
                      class="text-slate-400 group-hover:text-indigo-600 dark:group-hover:text-indigo-400 transition-colors"
                      title="Xem chi tiết">
                <i data-lucide="arrow-up-right" class="w-4 h-4"></i>
              </button>
            </div>

            <h4 class="font-bold text-sm text-slate-900 dark:text-white line-clamp-1 mb-2">
              ${course.name}
            </h4>

            <div class="space-y-1.5 text-xs text-slate-600 dark:text-slate-400">
              <div class="flex items-center gap-1.5 font-medium text-indigo-600 dark:text-indigo-400">
                <i data-lucide="clock" class="w-3.5 h-3.5 shrink-0"></i>
                <span>${tt.time || 'Tiết ' + (tt.startPeriod || 'N/A') + '-' + (tt.endPeriod || 'N/A')}</span>
              </div>
              <div class="flex items-center gap-1.5">
                <i data-lucide="map-pin" class="w-3.5 h-3.5 shrink-0 text-slate-400"></i>
                <span class="truncate">${tt.room || course.schedule || 'N/A'}</span>
              </div>
              <div class="flex items-center gap-1.5">
                <i data-lucide="user" class="w-3.5 h-3.5 shrink-0 text-slate-400"></i>
                <span class="truncate">${course.instructor ? course.instructor.name : 'N/A'}</span>
              </div>
            </div>
          </div>
        `;
      }).join('') : `
        <div class="py-8 text-center text-xs text-slate-400 dark:text-slate-600 font-medium">
          Không có tiết học
        </div>
      `;

      return `
        <div class="flex flex-col rounded-2xl border ${isToday ? 'border-indigo-500 ring-2 ring-indigo-500/20 shadow-md' : 'border-slate-200 dark:border-slate-800'} bg-slate-50/60 dark:bg-slate-900/40 p-4 transition-all">
          <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-200 dark:border-slate-800">
            <div class="flex items-center gap-2">
              <span class="font-bold text-base text-slate-900 dark:text-white">${d.name}</span>
            </div>
            ${isToday ? '<span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-indigo-600 text-white tracking-wider animate-pulse">Hôm nay</span>' : ''}
          </div>

          <div class="space-y-3 flex-1">
            ${coursesCardsHtml}
          </div>
        </div>
      `;
    }).join('');

    container.innerHTML = `
      <div class="flex items-center justify-between pb-2">
        <div>
          <h3 class="text-lg font-bold text-slate-900 dark:text-white">Lịch Học Trong Tuần</h3>
          <p class="text-xs text-slate-500 dark:text-slate-400">Thời khóa biểu chi tiết các ngày từ Thứ Hai đến Thứ Bảy</p>
        </div>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6 gap-4">
        ${dayColumnsHtml}
      </div>
    `;

    lucide.createIcons();
  }

  /**
   * TAB 4: RENDER SYLLABUS & ROADMAP
   */
  function renderSyllabusTab() {
    const container = document.getElementById('syllabus-container');
    if (!container || !semesterData) return;

    container.innerHTML = semesterData.courses.map(course => {
      const colorScheme = COLOR_MAP[course.badgeColor] || COLOR_MAP.indigo;
      const syllabus = course.syllabus || [];

      const listHtml = syllabus.map((item, idx) => {
        let statusBadge = '';
        let dotColor = 'bg-slate-300 dark:bg-slate-600';
        if (item.status === 'completed') {
          statusBadge = '<span class="text-xs font-medium text-emerald-600 dark:text-emerald-400 flex items-center gap-1"><i data-lucide="check" class="w-3.5 h-3.5"></i> Đã học</span>';
          dotColor = 'bg-emerald-500 ring-4 ring-emerald-100 dark:ring-emerald-950';
        } else if (item.status === 'in-progress') {
          statusBadge = '<span class="text-xs font-semibold text-amber-600 dark:text-amber-400 flex items-center gap-1"><i data-lucide="loader" class="w-3.5 h-3.5 animate-spin"></i> Đang học</span>';
          dotColor = 'bg-amber-500 ring-4 ring-amber-100 dark:ring-amber-950';
        } else {
          statusBadge = '<span class="text-xs text-slate-400">Sắp tới</span>';
        }

        return `
          <div class="relative pl-6 pb-6 last:pb-0">
            ${idx !== syllabus.length - 1 ? '<div class="absolute left-2.5 top-3.5 bottom-0 w-0.5 bg-slate-200 dark:bg-slate-800"></div>' : ''}
            <div class="absolute left-1 top-2 w-3.5 h-3.5 rounded-full ${dotColor}"></div>
            <div class="flex items-baseline justify-between gap-3">
              <div>
                <span class="text-xs font-bold text-slate-500 dark:text-slate-400">Tuần ${item.week || idx + 1}:</span>
                <span class="text-sm font-medium text-slate-800 dark:text-slate-200 ml-1.5">${item.topic}</span>
              </div>
              <div class="shrink-0">${statusBadge}</div>
            </div>
          </div>
        `;
      }).join('');

      return `
        <div class="rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 p-6 shadow-sm mb-6">
          <div class="flex items-center justify-between pb-4 mb-5 border-b border-slate-100 dark:border-slate-800">
            <div>
              <span class="text-xs font-semibold ${colorScheme.badge} px-2.5 py-0.5 rounded-full">${course.name}</span>
              <h3 class="text-lg font-bold text-slate-900 dark:text-white mt-1">${course.name}</h3>
            </div>
            <button onclick="window.SemesterApp.openCourseDetail('${course.id}')" 
                    class="text-xs font-medium text-indigo-600 dark:text-indigo-400 hover:underline">
              Chi tiết đề cương
            </button>
          </div>
          <div>${listHtml}</div>
        </div>
      `;
    }).join('');

    lucide.createIcons();
  }

  /**
   * TAB 5: RENDER RESOURCES & QUICK LINKS
   */
  function renderResourcesTab() {
    const container = document.getElementById('resources-container');
    if (!container || !semesterData) return;

    // General portals
    const generalLinksHtml = (semesterData.quickLinks || []).map(link => `
      <a href="${link.url}" target="_blank" rel="noopener noreferrer"
         class="flex items-start gap-4 p-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 hover:shadow-md hover:border-indigo-300 dark:hover:border-indigo-700 transition-all duration-200">
        <div class="p-3 rounded-xl bg-indigo-50 text-indigo-600 dark:bg-indigo-950/60 dark:text-indigo-400 shrink-0">
          <i data-lucide="${link.icon || 'link'}" class="w-6 h-6"></i>
        </div>
        <div>
          <h4 class="font-bold text-slate-900 dark:text-white text-base flex items-center gap-1.5">
            ${link.title}
            <i data-lucide="external-link" class="w-3.5 h-3.5 text-slate-400"></i>
          </h4>
          <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">${link.desc || link.url}</p>
        </div>
      </a>
    `).join('');

    // Course specific links
    const courseLinksHtml = semesterData.courses.map(course => {
      const colorScheme = COLOR_MAP[course.badgeColor] || COLOR_MAP.indigo;
      const links = course.links || [];
      if (links.length === 0) return '';

      const items = links.map(l => `
        <a href="${l.url}" target="_blank" rel="noopener noreferrer"
           class="flex items-center justify-between p-3 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200/80 dark:border-slate-700/60 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors">
          <span class="text-xs font-semibold text-slate-700 dark:text-slate-300 flex items-center gap-2">
            <i data-lucide="${getLinkIcon(l.type || l.title)}" class="w-4 h-4 text-indigo-500"></i>
            ${l.title}
          </span>
          <i data-lucide="external-link" class="w-3.5 h-3.5 text-slate-400"></i>
        </a>
      `).join('');

      return `
        <div class="p-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
          <div class="flex items-center gap-2 mb-3">
            <span class="text-xs font-bold ${colorScheme.badge} px-2 py-0.5 rounded">${course.code}</span>
            <h4 class="font-bold text-slate-900 dark:text-white text-sm truncate">${course.name}</h4>
          </div>
          <div class="space-y-2">${items}</div>
        </div>
      `;
    }).join('');

    container.innerHTML = `
      <div class="mb-8">
        <h3 class="text-lg font-bold text-slate-900 dark:text-white mb-4">Cổng Thông Tin & Nền Tảng Dùng Chung</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          ${generalLinksHtml}
        </div>
      </div>

      <div>
        <h3 class="text-lg font-bold text-slate-900 dark:text-white mb-4">Tài Liệu Theo Từng Học Phần</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          ${courseLinksHtml}
        </div>
      </div>
    `;

    lucide.createIcons();
  }

  /**
   * MODAL: COURSE DETAIL (Accessible <dialog>)
   */
  function openCourseDetail(courseId) {
    const course = semesterData.courses.find(c => c.id === courseId);
    if (!course) return;

    activeCourse = course;
    activeChapter = null;
    activeCourseTaskId = null;
    const title = document.getElementById('course-detail-title');
    if (title) title.textContent = course.name;
    document.getElementById('semester-overview').classList.add('hidden');
    document.getElementById('semester-navigation').classList.add('hidden');
    ['tab-courses', 'tab-tasks', 'tab-timetable', 'tab-syllabus', 'tab-resources', 'chapter-detail', 'course-task-detail'].forEach(id => {
      document.getElementById(id)?.classList.add('hidden');
    });
    document.getElementById('course-detail').classList.remove('hidden');
    renderCourseChapterList();
    lucide.createIcons();
  }

  function closeCourseDetail() {
    activeCourse = null;
    activeChapter = null;
    activeCourseTaskId = null;
    setActiveTab('courses');
  }

  function renderCourseChapterList() {
    const container = document.getElementById('course-chapters-list');
    if (!container || !activeCourse) return;
    const chapters = activeCourse.chapters || [];
    if (chapters.length === 0) {
      container.innerHTML = '<p class="py-8 text-base text-slate-500 dark:text-slate-400">Chưa có chương được cập nhật.</p>';
      return;
    }

    container.innerHTML = chapters.map((chapter, index) => `
      <button type="button" onclick="window.SemesterApp.openChapterDetail('${chapter.id}')"
              class="group w-full flex items-center gap-4 py-5 text-left border-b border-slate-200 dark:border-slate-800 hover:bg-indigo-50/60 dark:hover:bg-slate-800/60 transition-colors">
        <span class="w-10 h-10 shrink-0 flex items-center justify-center rounded-lg bg-indigo-50 dark:bg-indigo-950/60 text-sm font-bold text-indigo-600 dark:text-indigo-400">${String(index + 1).padStart(2, '0')}</span>
        <span class="flex-1 min-w-0">
          <span class="block text-base font-bold text-slate-900 dark:text-white group-hover:text-indigo-600 dark:group-hover:text-indigo-400">${chapter.title}</span>
          <span class="block mt-1 text-sm text-slate-500 dark:text-slate-400">${chapter.tasks.length} task</span>
        </span>
        <i data-lucide="chevron-right" class="w-5 h-5 shrink-0 text-slate-400 group-hover:text-indigo-500"></i>
      </button>
    `).join('');
  }

  function openChapterDetail(chapterId) {
    if (!activeCourse) return;
    activeChapter = activeCourse.chapters.find(chapter => chapter.id === chapterId);
    if (!activeChapter) return;
    activeChapterTab = 'content';
    activeCourseTaskId = null;
    document.getElementById('course-detail').classList.add('hidden');
    document.getElementById('course-task-detail').classList.add('hidden');
    document.getElementById('chapter-detail').classList.remove('hidden');
    document.getElementById('chapter-detail-title').textContent = activeChapter.title;
    document.getElementById('chapter-detail-course').textContent = activeCourse.name;
    setChapterTab('content');
  }

  function returnToCourseDetail() {
    activeChapter = null;
    activeCourseTaskId = null;
    document.getElementById('chapter-detail').classList.add('hidden');
    document.getElementById('course-task-detail').classList.add('hidden');
    document.getElementById('course-detail').classList.remove('hidden');
    renderCourseChapterList();
  }

  function setChapterTab(tabKey) {
    activeChapterTab = tabKey;
    document.querySelectorAll('.chapter-tab').forEach(button => {
      const isCurrent = button.dataset.chapterTab === tabKey;
      button.className = isCurrent
        ? 'chapter-tab px-4 py-3 text-sm font-bold text-indigo-600 dark:text-indigo-400 border-b-2 border-indigo-600 dark:border-indigo-400 flex items-center gap-2'
        : 'chapter-tab px-4 py-3 text-sm font-medium text-slate-500 hover:text-slate-800 dark:hover:text-slate-200 border-b-2 border-transparent flex items-center gap-2';
    });

    const panel = document.getElementById('chapter-detail-panel');
    if (!panel || !activeChapter) return;
    if (tabKey === 'content') renderChapterContent(panel);
    else renderChapterTasks(panel);
    lucide.createIcons();
  }

  function renderChapterContent(container) {
    const content = activeChapter.content || '_Chương này chưa có nội dung._';
    container.innerHTML = `<article class="markdown-body prose prose-lg dark:prose-invert max-w-4xl text-base leading-8">${DOMPurify.sanitize(marked.parse(content))}</article>`;
  }

  function renderChapterTasks(container) {
    const tasks = activeChapter.tasks || [];
    if (tasks.length === 0) {
      container.innerHTML = '<p class="py-8 text-base text-slate-500 dark:text-slate-400">Chương này chưa có task.</p>';
      return;
    }

    const items = tasks.map((task, index) => `
      <button type="button" onclick="window.SemesterApp.openCourseTaskDetail('${task.id}')"
              class="group w-full flex items-center gap-4 px-4 py-5 text-left border-b border-slate-200 dark:border-slate-800 hover:bg-indigo-50/60 dark:hover:bg-slate-800/60 transition-colors">
        <span class="w-10 h-10 shrink-0 flex items-center justify-center rounded-lg bg-slate-100 dark:bg-slate-800 text-sm font-bold text-slate-500 dark:text-slate-400">${String(index + 1).padStart(2, '0')}</span>
        <span class="flex-1 min-w-0 text-base font-semibold text-slate-800 dark:text-slate-200 group-hover:text-indigo-600 dark:group-hover:text-indigo-400">${task.title}</span>
        <span class="w-2.5 h-2.5 shrink-0 rounded-full ${task.status === 'done' ? 'bg-emerald-500' : task.status === 'in-progress' ? 'bg-amber-400' : 'bg-slate-300 dark:bg-slate-600'}" aria-label="${task.status === 'done' ? 'Đã hoàn thành' : task.status === 'in-progress' ? 'Đang làm' : 'Cần làm'}"></span>
        <i data-lucide="chevron-right" class="w-5 h-5 shrink-0 text-slate-400 group-hover:text-indigo-500"></i>
      </button>
    `).join('');

    container.innerHTML = `<div class="overflow-hidden border-t border-slate-200 dark:border-slate-800">${items}</div>`;
  }

  function updateChapterTasks() {
    if (activeChapter && activeChapterTab === 'tasks') {
      const panel = document.getElementById('chapter-detail-panel');
      if (panel) renderChapterTasks(panel);
      if (activeCourseTaskId) renderCourseTaskDetail();
      lucide.createIcons();
    }
  }

  function openCourseTaskDetail(taskId) {
    if (!activeChapter) return;
    activeCourseTaskId = taskId;
    document.getElementById('chapter-detail').classList.add('hidden');
    document.getElementById('course-task-detail').classList.remove('hidden');
    renderCourseTaskDetail();
    lucide.createIcons();
  }

  function returnToChapterTasks() {
    activeCourseTaskId = null;
    document.getElementById('course-task-detail').classList.add('hidden');
    document.getElementById('chapter-detail').classList.remove('hidden');
    setChapterTab('tasks');
  }

  function renderCourseTaskDetail() {
    const task = activeChapter?.tasks.find(item => item.id === activeCourseTaskId);
    if (!task) return;

    const chapterTitle = document.getElementById('course-task-chapter');
    const title = document.getElementById('course-task-title');
    const content = document.getElementById('course-task-content');
    const deadline = document.getElementById('course-task-deadline');
    const priority = document.getElementById('course-task-priority');
    const status = document.getElementById('course-task-status');

    if (chapterTitle) chapterTitle.textContent = activeChapter.title;
    if (title) title.textContent = task.title;
    if (content) {
      const note = task.note || 'Task này chưa có mô tả.';
      content.innerHTML = DOMPurify.sanitize(marked.parse(note));
    }
    if (deadline) deadline.textContent = task.deadline || 'Chưa đặt hạn';
    if (priority) priority.textContent = task.priority === 'high' ? 'Cao' : task.priority === 'low' ? 'Thấp' : 'Trung bình';
    if (status) status.value = task.status || 'todo';
  }

  function setCourseTaskStatus(status) {
    if (!activeCourseTaskId) return;
    saveTaskStatus(activeCourseTaskId, status);
  }

  /**
   * MODAL: ADD TASK LOGIC
   */
  function populateTaskChapterOptions(courseId, selectedChapterId = '') {
    const chapterSelect = document.getElementById('modal-task-chapter');
    const course = semesterData.courses.find(item => item.id === courseId);
    if (!chapterSelect || !course) return;

    if (course.chapters.length === 0) {
      chapterSelect.innerHTML = '<option value="">Chưa có chương (sẽ tạo chương mặc định)</option>';
      return;
    }

    chapterSelect.innerHTML = course.chapters.map(chapter =>
      `<option value="${chapter.id}">${chapter.title}</option>`
    ).join('');
    chapterSelect.value = course.chapters.some(chapter => chapter.id === selectedChapterId)
      ? selectedChapterId
      : course.chapters[0].id;
  }

  function openAddTaskModal(preselectedCourseId = null) {
    const modal = document.getElementById('add-task-modal');
    const courseSelect = document.getElementById('modal-task-course');
    if (!modal || !semesterData) return;

    if (courseSelect) {
      courseSelect.innerHTML = semesterData.courses.map(c => 
        `<option value="${c.id}" ${preselectedCourseId === c.id ? 'selected' : ''}>${c.name}</option>`
      ).join('');
      populateTaskChapterOptions(courseSelect.value);
    }

    // Set tomorrow as default deadline
    const tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    const deadlineInput = document.getElementById('modal-task-deadline');
    if (deadlineInput) {
      deadlineInput.value = tomorrow.toISOString().split('T')[0];
    }

    modal.showModal();
    lucide.createIcons();
  }

  function closeAddTaskModal() {
    const modal = document.getElementById('add-task-modal');
    if (modal) modal.close();
  }

  function handleAddTaskSubmit(e) {
    e.preventDefault();
    const courseId = document.getElementById('modal-task-course').value;
    const chapterId = document.getElementById('modal-task-chapter').value;
    const title = document.getElementById('modal-task-title').value.trim();
    const deadline = document.getElementById('modal-task-deadline').value;
    const priority = document.getElementById('modal-task-priority').value;
    const status = document.getElementById('modal-task-status').value;
    const note = document.getElementById('modal-task-note').value.trim();

    if (!title || !courseId) return;

    const targetCourse = semesterData.courses.find(course => course.id === courseId);
    if (!targetCourse) return;
    const targetChapter = targetCourse.chapters.find(chapter => chapter.id === chapterId) ||
      ensureUncategorizedChapter(targetCourse);

    const newTask = {
      id: 'task-custom-' + Date.now(),
      courseId: courseId,
      chapterId: targetChapter.id,
      title: title,
      deadline: deadline,
      priority: priority,
      status: status,
      note: note
    };

    targetChapter.tasks.push(newTask);

    // Save to custom tasks in localStorage
    const customTasks = getStoredCustomTasks();
    customTasks.push(newTask);
    localStorage.setItem(LS_CUSTOM_TASKS, JSON.stringify(customTasks));

    // Also persist status
    saveTaskStatus(newTask.id, status);

    closeAddTaskModal();
    showToast('Đã thêm task mới thành công!');

    renderStats();
    if (activeTab === 'tasks') renderTasksTab();
    if (activeTab === 'courses') renderCoursesTab();
  }

  /**
   * EXPORT / SYNC HELPER (For Git-based updates)
   */
  function openExportModal() {
    const modal = document.getElementById('export-modal');
    const textarea = document.getElementById('export-code-area');
    if (!modal || !textarea) return;

    // Generate Javascript code format for data/courses.js
    const code = `// Cập nhật ngày: ${new Date().toLocaleString('vi-VN')}\nwindow.SEMESTER_DATA = ${JSON.stringify(semesterData, null, 2)};\n`;
    textarea.value = code;

    modal.showModal();
    lucide.createIcons();
  }

  function closeExportModal() {
    const modal = document.getElementById('export-modal');
    if (modal) modal.close();
  }

  function copyExportCode() {
    const textarea = document.getElementById('export-code-area');
    const copyBtn = document.getElementById('btn-copy-code');
    if (!textarea) return;

    navigator.clipboard.writeText(textarea.value).then(() => {
      showToast('Đã sao chép mã nguồn vào clipboard!');
      if (copyBtn) {
        copyBtn.innerHTML = '<i data-lucide="check" class="w-4 h-4 text-emerald-500"></i> Đã sao chép!';
        lucide.createIcons();
        setTimeout(() => {
          copyBtn.innerHTML = '<i data-lucide="copy" class="w-4 h-4"></i> Sao chép mã nguồn';
          lucide.createIcons();
        }, 2000);
      }
    });
  }

  function downloadCoursesFile() {
    const code = `/**\n * Cập nhật ngày: ${new Date().toLocaleString('vi-VN')}\n */\nwindow.SEMESTER_DATA = ${JSON.stringify(semesterData, null, 2)};\n`;
    const blob = new Blob([code], { type: 'text/javascript;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'courses.js';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    showToast('Đã tải file courses.js về máy!');
  }

  /**
   * Toast notification helper
   */
  let toastTimer = null;
  function showToast(message, type = 'success') {
    const toast = document.getElementById('toast');
    const msgEl = document.getElementById('toast-message');
    if (!toast || !msgEl) return;

    msgEl.textContent = message;
    toast.classList.remove('translate-y-20', 'opacity-0', 'pointer-events-none');
    toast.classList.add('translate-y-0', 'opacity-100');

    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      toast.classList.add('translate-y-20', 'opacity-0', 'pointer-events-none');
      toast.classList.remove('translate-y-0', 'opacity-100');
    }, 3200);
  }

  /**
   * Theme toggler
   */
  function initTheme() {
    const saved = localStorage.getItem(LS_THEME);
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

    if (saved === 'dark' || (!saved && prefersDark)) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }

  function toggleTheme() {
    const isDark = document.documentElement.classList.toggle('dark');
    localStorage.setItem(LS_THEME, isDark ? 'dark' : 'light');
    lucide.createIcons();
  }

  /**
   * Main App Initialization & Event Listeners
   */
  function initApp() {
    initTheme();
    initData();
    renderStats();
    renderCoursesTab();

    // Setup Tab Navigation
    document.querySelectorAll('.nav-tab').forEach(btn => {
      btn.addEventListener('click', e => {
        const tab = e.currentTarget.dataset.tab;
        setActiveTab(tab);
      });
    });

    // Setup Global Search
    const searchInput = document.getElementById('global-search');
    if (searchInput) {
      searchInput.addEventListener('input', e => {
        searchQuery = e.target.value;
        if (activeTab === 'courses') renderCoursesTab();
        else if (activeTab === 'tasks') renderTasksTab();
      });
    }

    // Setup Task Filters
    document.querySelectorAll('.task-filter-btn').forEach(btn => {
      btn.addEventListener('click', e => {
        document.querySelectorAll('.task-filter-btn').forEach(b => {
          b.className = 'task-filter-btn px-3 py-1.5 text-xs font-semibold rounded-lg bg-slate-100 text-slate-600 dark:bg-slate-800 dark:text-slate-400 hover:bg-slate-200 dark:hover:bg-slate-700 transition-colors';
        });
        e.currentTarget.className = 'task-filter-btn px-3 py-1.5 text-xs font-semibold rounded-lg bg-indigo-600 text-white shadow-sm transition-colors';
        taskFilter = e.currentTarget.dataset.filter;
        renderTasksTab();
      });
    });

    // Setup Task Course Filter Select
    const courseSelect = document.getElementById('task-course-filter');
    if (courseSelect) {
      courseSelect.addEventListener('change', e => {
        taskCourseFilter = e.target.value;
        renderTasksTab();
      });
    }

    const modalCourseSelect = document.getElementById('modal-task-course');
    if (modalCourseSelect) {
      modalCourseSelect.addEventListener('change', e => {
        populateTaskChapterOptions(e.target.value);
      });
    }

    // Setup View Mode Switcher
    const btnViewCourse = document.getElementById('btn-view-course');
    const btnViewKanban = document.getElementById('btn-view-kanban');
    if (btnViewCourse && btnViewKanban) {
      btnViewCourse.addEventListener('click', () => {
        taskViewMode = 'by-course';
        btnViewCourse.className = 'p-1.5 rounded-lg bg-white dark:bg-slate-700 text-indigo-600 dark:text-indigo-400 shadow-sm';
        btnViewKanban.className = 'p-1.5 rounded-lg text-slate-500 hover:text-slate-900 dark:hover:text-slate-100';
        renderTasksTab();
      });
      btnViewKanban.addEventListener('click', () => {
        taskViewMode = 'kanban';
        btnViewKanban.className = 'p-1.5 rounded-lg bg-white dark:bg-slate-700 text-indigo-600 dark:text-indigo-400 shadow-sm';
        btnViewCourse.className = 'p-1.5 rounded-lg text-slate-500 hover:text-slate-900 dark:hover:text-slate-100';
        renderTasksTab();
      });
    }

    // Setup Modal Light-Dismiss (clicking backdrop closes dialog)
    const modals = [
      document.getElementById('export-modal'),
      document.getElementById('add-task-modal')
    ];
    modals.forEach(m => {
      if (m) {
        m.addEventListener('click', e => {
          const rect = m.getBoundingClientRect();
          const isInDialog = (
            rect.top <= e.clientY &&
            e.clientY <= rect.top + rect.height &&
            rect.left <= e.clientX &&
            e.clientX <= rect.left + rect.width
          );
          if (!isInDialog) {
            m.close();
          }
        });
      }
    });

    lucide.createIcons();
  }

  function setActiveTab(tab) {
    activeTab = tab;
    document.getElementById('semester-overview').classList.remove('hidden');
    document.getElementById('semester-navigation').classList.remove('hidden');

    // Update active nav button
    document.querySelectorAll('.nav-tab').forEach(btn => {
      const isCurrent = btn.dataset.tab === tab;
      if (isCurrent) {
        btn.className = 'nav-tab flex items-center gap-2 px-4 py-2.5 rounded-xl font-bold text-sm bg-indigo-600 text-white shadow-sm transition-all';
      } else {
        btn.className = 'nav-tab flex items-center gap-2 px-4 py-2.5 rounded-xl font-medium text-sm text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 transition-all';
      }
    });

    // Hide all tab views
    ['tab-courses', 'tab-tasks', 'tab-timetable', 'tab-syllabus', 'tab-resources', 'course-detail', 'chapter-detail', 'course-task-detail'].forEach(id => {
      const el = document.getElementById(id);
      if (el) el.classList.add('hidden');
    });

    // Show target tab
    const targetEl = document.getElementById(`tab-${tab}`);
    if (targetEl) targetEl.classList.remove('hidden');

    if (tab === 'courses') renderCoursesTab();
    else if (tab === 'tasks') renderTasksTab();
    else if (tab === 'timetable') renderTimetableTab();
    else if (tab === 'syllabus') renderSyllabusTab();
    else if (tab === 'resources') renderResourcesTab();

    lucide.createIcons();
  }

  // Expose global methods for inline HTML event handlers
  window.SemesterApp = {
    toggleTheme,
    setActiveTab,
    openCourseDetail,
    closeCourseDetail,
    openChapterDetail,
    returnToCourseDetail,
    setChapterTab,
    openCourseTaskDetail,
    returnToChapterTasks,
    setCourseTaskStatus,
    openAddTaskModal,
    closeAddTaskModal,
    handleAddTaskSubmit,
    openExportModal,
    closeExportModal,
    copyExportCode,
    downloadCoursesFile,
    changeTaskSort,
    showToast,
    toggleTask: (taskId, isChecked) => {
      saveTaskStatus(taskId, isChecked ? 'done' : 'todo');
      showToast(isChecked ? 'Đã hoàn thành task! 🎉' : 'Đã chuyển sang chưa xong');
    },
    updateTaskStatus: (taskId, newStatus) => {
      saveTaskStatus(taskId, newStatus);
      showToast('Đã cập nhật trạng thái task!');
    }
  };

  // Run on DOM Ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initApp);
  } else {
    initApp();
  }
})();
