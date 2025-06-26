// WLTP World API - Frontend JavaScript

class WLTPAPI {
    constructor() {
        this.baseURL = window.location.origin;
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.loadInitialData();
    }

    setupEventListeners() {
        // API 링크 클릭 이벤트
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('api-link')) {
                e.preventDefault();
                this.handleAPILink(e.target.href);
            }
        });

        // 검색 기능
        const searchInput = document.querySelector('#search-input');
        if (searchInput) {
            searchInput.addEventListener('input', (e) => {
                this.handleSearch(e.target.value);
            });
        }

        // 필터 기능
        const filterButtons = document.querySelectorAll('.filter-btn');
        filterButtons.forEach(btn => {
            btn.addEventListener('click', (e) => {
                this.handleFilter(e.target.dataset.filter);
            });
        });
    }

    async loadInitialData() {
        try {
            // 서버 정보 로드
            const serverInfo = await this.fetchAPI('/api/server/info');
            this.displayServerInfo(serverInfo);

            // 통계 정보 로드
            const stats = await this.fetchAPI('/api/stats');
            this.displayStats(stats);
        } catch (error) {
            console.error('초기 데이터 로드 실패:', error);
        }
    }

    async fetchAPI(endpoint, options = {}) {
        try {
            const response = await fetch(`${this.baseURL}${endpoint}`, {
                headers: {
                    'Content-Type': 'application/json',
                    ...options.headers
                },
                ...options
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error(`API 요청 실패 (${endpoint}):`, error);
            throw error;
        }
    }

    async handleAPILink(url) {
        const endpoint = new URL(url).pathname;
        
        try {
            this.showLoading();
            const data = await this.fetchAPI(endpoint);
            this.displayAPIResponse(endpoint, data);
        } catch (error) {
            this.showError(`API 요청 실패: ${error.message}`);
        } finally {
            this.hideLoading();
        }
    }

    displayAPIResponse(endpoint, data) {
        const container = document.querySelector('.container');
        
        // 기존 응답 제거
        const existingResponse = document.querySelector('.api-response');
        if (existingResponse) {
            existingResponse.remove();
        }

        const responseDiv = document.createElement('div');
        responseDiv.className = 'api-response fade-in';
        
        const title = this.getEndpointTitle(endpoint);
        responseDiv.innerHTML = `
            <h2>${title}</h2>
            <div class="json-display">${JSON.stringify(data, null, 2)}</div>
            <div class="response-actions">
                <button onclick="this.parentElement.parentElement.remove()" class="btn">닫기</button>
                <button onclick="api.displayFormatted('${endpoint}', ${JSON.stringify(data).replace(/"/g, '&quot;')})" class="btn">포맷된 보기</button>
            </div>
        `;

        container.appendChild(responseDiv);
    }

    displayFormatted(endpoint, data) {
        const container = document.querySelector('.container');
        
        // 기존 응답 제거
        const existingResponse = document.querySelector('.api-response');
        if (existingResponse) {
            existingResponse.remove();
        }

        const responseDiv = document.createElement('div');
        responseDiv.className = 'api-response fade-in';
        
        const title = this.getEndpointTitle(endpoint);
        let formattedContent = '';

        switch (endpoint) {
            case '/api/players':
                formattedContent = this.formatPlayers(data);
                break;
            case '/api/ranking/build':
                formattedContent = this.formatRanking(data);
                break;
            case '/api/notices':
                formattedContent = this.formatNotices(data);
                break;
            case '/api/gallery':
                formattedContent = this.formatGallery(data);
                break;
            default:
                formattedContent = `<div class="json-display">${JSON.stringify(data, null, 2)}</div>`;
        }

        responseDiv.innerHTML = `
            <h2>${title}</h2>
            ${formattedContent}
            <div class="response-actions">
                <button onclick="this.parentElement.parentElement.remove()" class="btn">닫기</button>
            </div>
        `;

        container.appendChild(responseDiv);
    }

    formatPlayers(players) {
        return `
            <div class="players-grid">
                ${players.map(player => `
                    <div class="player-card">
                        <div class="player-header">
                            <span class="player-name">${player.username}</span>
                            <span class="player-level">${player.level}</span>
                        </div>
                        <div class="player-stats">
                            <div class="stat-item">
                                <div class="stat-value">${player.build_count}</div>
                                <div class="stat-label">빌드 수</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-value">${player.avg_score}</div>
                                <div class="stat-label">평균 점수</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-value">${player.total_score}</div>
                                <div class="stat-label">총 점수</div>
                            </div>
                        </div>
                        <div class="player-best">
                            <strong>최고 빌드:</strong> ${player.best_build}
                        </div>
                    </div>
                `).join('')}
            </div>
        `;
    }

    formatRanking(ranking) {
        return `
            <table class="ranking-table">
                <thead>
                    <tr>
                        <th>순위</th>
                        <th>플레이어</th>
                        <th>레벨</th>
                        <th>빌드 수</th>
                        <th>평균 점수</th>
                        <th>총 점수</th>
                        <th>최고 빌드</th>
                    </tr>
                </thead>
                <tbody>
                    ${ranking.map(item => `
                        <tr>
                            <td class="rank-${item.rank}">${item.rank}</td>
                            <td>${item.player.username}</td>
                            <td>${item.player.level}</td>
                            <td>${item.player.build_count}</td>
                            <td>${item.player.avg_score}</td>
                            <td>${item.player.total_score}</td>
                            <td>${item.player.best_build}</td>
                        </tr>
                    `).join('')}
                </tbody>
            </table>
        `;
    }

    formatNotices(notices) {
        return `
            <div class="notices-grid">
                ${notices.map(notice => `
                    <div class="notice-card">
                        <div class="notice-header">
                            <span class="notice-category">${notice.category}</span>
                            <span class="notice-date">${notice.date}</span>
                        </div>
                        <div class="notice-title">${notice.title}</div>
                        <div class="notice-content">${notice.content}</div>
                        <div class="notice-footer">
                            <span class="notice-author">${notice.author}</span>
                            <span class="notice-views">조회수: ${notice.views}</span>
                        </div>
                    </div>
                `).join('')}
            </div>
        `;
    }

    formatGallery(gallery) {
        return `
            <div class="gallery-grid">
                ${gallery.map(item => `
                    <div class="gallery-item">
                        <div class="gallery-image">
                            ${item.image_url ? `<img src="${item.image_url}" alt="${item.title}">` : '이미지 없음'}
                        </div>
                        <div class="gallery-info">
                            <div class="gallery-title">${item.title}</div>
                            <div class="gallery-builder">${item.builder}</div>
                            <span class="gallery-score">${item.score}점</span>
                        </div>
                    </div>
                `).join('')}
            </div>
        `;
    }

    displayServerInfo(serverInfo) {
        const container = document.querySelector('.server-info');
        if (container) {
            container.innerHTML = `
                <div class="server-info-card">
                    <h3>서버 정보</h3>
                    <div class="server-info-grid">
                        <div class="info-item">
                            <div class="info-label">서버 주소</div>
                            <div class="info-value">${serverInfo.address}</div>
                        </div>
                        <div class="info-item">
                            <div class="info-label">버전</div>
                            <div class="info-value">${serverInfo.version}</div>
                        </div>
                        <div class="info-item">
                            <div class="info-label">온라인 플레이어</div>
                            <div class="info-value">${serverInfo.online_players}/${serverInfo.max_players}</div>
                        </div>
                        <div class="info-item">
                            <div class="info-label">운영시간</div>
                            <div class="info-value">${serverInfo.uptime}</div>
                        </div>
                    </div>
                </div>
            `;
        }
    }

    displayStats(stats) {
        const container = document.querySelector('.server-stats');
        if (container) {
            container.innerHTML = `
                <div class="stats-card">
                    <h3>서버 통계</h3>
                    <div class="stats-grid">
                        <div class="stat-item">
                            <div class="stat-value">${stats.total_players}</div>
                            <div class="stat-label">총 플레이어</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-value">${stats.total_builds}</div>
                            <div class="stat-label">총 빌드</div>
                        </div>
                        <div class="stat-item">
                            <div class="stat-value">${stats.avg_score.toFixed(1)}</div>
                            <div class="stat-label">평균 점수</div>
                        </div>
                    </div>
                </div>
            `;
        }
    }

    getEndpointTitle(endpoint) {
        const titles = {
            '/api/players': '플레이어 목록',
            '/api/ranking/build': '빌드 랭킹',
            '/api/notices': '공지사항',
            '/api/gallery': '갤러리',
            '/api/server/info': '서버 정보',
            '/api/stats': '서버 통계'
        };
        return titles[endpoint] || 'API 응답';
    }

    handleSearch(query) {
        // 검색 기능 구현
        console.log('검색:', query);
    }

    handleFilter(filter) {
        // 필터 기능 구현
        console.log('필터:', filter);
    }

    showLoading() {
        const loading = document.createElement('div');
        loading.className = 'loading-overlay';
        loading.innerHTML = '<div class="loading"></div>';
        document.body.appendChild(loading);
    }

    hideLoading() {
        const loading = document.querySelector('.loading-overlay');
        if (loading) {
            loading.remove();
        }
    }

    showError(message) {
        const error = document.createElement('div');
        error.className = 'error-message';
        error.textContent = message;
        document.body.appendChild(error);
        
        setTimeout(() => {
            error.remove();
        }, 3000);
    }
}

// API 인스턴스 생성
const api = new WLTPAPI();

// 전역 함수로 노출
window.api = api; 