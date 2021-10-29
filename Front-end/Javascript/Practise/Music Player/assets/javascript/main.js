// 1. Render songs
// 2. Scroll top
// 3. Play/ Pause/ Seek 
// 4. CD rotate 
// 5. Next/ Previous
// 6. Random
// 7. Active songs
// 8. Scroll active song into view 
// 9. Scroll active song into view 
// 10. Play song when click 
const $ = document.querySelector.bind(document);
const $$ = document.querySelectorAll.bind(document);

const PLAYER_STORAGE_KEY = 'F8_PLAYER'

const heading = $('header h2')
const cdThumb = $('.cd-thumb')
const audio = $('#audio')
const cd = $('.cd');
const player = $('.player')
const playButton = $('.btn-toggle-play')
const progress = $('#progress')
const nextButton = $('.btn-next')
const prevButton = $('.btn-prev')
const randomButton = $('.btn-random')
const repeatButton = $('.btn-repeat')
const playlist = $('.playlist')

const app = {
    currentIndex: 0,
    config: JSON.parse(localStorage.getItem(PLAYER_STORAGE_KEY)) || {},
    setConfig: function(key, value) {
        this.config[key] = value;
        localStorage.setItem(PLAYER_STORAGE_KEY, JSON.stringify(this.config))
    },
    songs: [
        {
            name: 'Ghé qua',
            singer: 'BCTM',
            path: './assets/songs/song0.mp3',
            image: './assets/img/song0.jpg'
        },
        {
            name: 'Lạ quá',
            singer: 'Karik & B Ray',
            path: './assets/songs/song1.mp3',
            image: './assets/img/song1.jpg'
        },
        {
            name: 'Loser',
            singer: 'BIGBANG',
            path: './assets/songs/song2.mp3',
            image: './assets/img/song23.jfif'
        },
        {
            name: 'Let\'s not fall in love',
            singer: 'BIGBANG',
            path: './assets/songs/song3.mp3',
            image: './assets/img/song23.jfif'
        },
        {
            name: 'Em đã thương người ta hơn anh',
            singer: 'Noo Phước Thịnh',
            path: './assets/songs/song4.mp3',
            image: './assets/img/song4.jfif'
        },
        {
            name: 'Thuận theo ý trời',
            singer: 'Bùi Anh Tuấn',
            path: './assets/songs/song5.mp3',
            image: './assets/img/song5.jpg'
        },
        {
            name: 'Có hẹn với thanh xuân',
            singer: 'MONSTAR',
            path: './assets/songs/song6.mp3',
            image: './assets/img/song6.jpg'
        },
        {
            name: 'Thức giấc',
            singer: 'DALAB',
            path: './assets/songs/song7.mp3',
            image: './assets/img/song7.jfif'
        },
        {
            name: '3107 3',
            singer: 'Duongg, Nâu, W/n',
            path: './assets/songs/song8.mp3',
            image: './assets/img/song8.jpg'
        },
        {
            name: 'Hãy trao cho anh',
            singer: 'Sơn Tùng MTP',
            path: './assets/songs/song9.mp3',
            image: './assets/img/song9.jfif'
        },
    ],
// Render songs
    render: function() {
        const htmls = this.songs.map((song, index) => {
            return `
                <div class="song ${index === this.currentIndex ? 'active' : ''}" data-index="${index}">
                    <div class="thumb" style="background-image: url('${song.image}')">
                    </div>
                    <div class="body">
                        <h3 class="title">${song.name}</h3>
                        <p class="author">${song.singer}</p>
                    </div>
                    <div class="option">
                        <i class="fas fa-ellipsis-h"></i>
                    </div>
                </div>`
        })
        playlist.innerHTML = htmls.join('')
    },

    defineProperties: function() {
        Object.defineProperty(this, 'currentSong', {
            get: function() {
                return this.songs[this.currentIndex]
            }
        })
    },
    isPlaying: false,
    isRandom: false,
    isRepeat: false,
    handleEvents: function() {
        const _this = this
        // CD Rotate
        const cdThumbAnimate = cdThumb.animate([
            { transform: 'rotate(360deg)'}
        ], {
            duration: 10000,
            iterations: Infinity
        })

        cdThumbAnimate.pause()

        // Scroll top
        const cdWidth = cd.offsetWidth;
        document.onscroll = function() {
            const scrollTop = window.scrollY
            const newcdWidth = cdWidth - scrollTop

            cd.style.width = newcdWidth > 0 ? newcdWidth + 'px' :0
            cd.style.opacity = newcdWidth / scrollTop 
        }

        // Play/ Pause/ Seek 
        playButton.onclick = function() {
            if (_this.isPlaying) {
                audio.pause()
            } else {
                audio.play()
            }
            audio.onplay = function() {
                _this.isPlaying = true
                player.classList.add('playing')
                cdThumbAnimate.play()
            }

            audio.onpause = function() {
                _this.isPlaying = false
                player.classList.remove('playing')
                cdThumbAnimate.pause()
            }

            // timeline
            audio.ontimeupdate = function() {
                if (audio.duration) {
                    const progressPercent = Math.floor(audio.currentTime / audio.duration *100)
                    progress.value = progressPercent
                }
            }

            // Seek
            progress.onchange = function(e) {
                const seekTime = e.target.value * audio.duration /100
                audio.currentTime = seekTime
            }

            // Next
            nextButton.onclick = function() {
                if (_this.isRandom) {
                    _this.playRandomSong()
                } else {
                    _this.nextSong()
                }
                audio.play()
                _this.render()
                _this.scrolltoActiveSong()
            }

            // Previous
            prevButton.onclick = function() {
                if (_this.isRandom) {
                _this.playRandomSong()
                } else {
                    _this.prevSong()
                }
                audio.play()
                _this.render()
                _this.scrolltoActiveSong()
            }

            // Random
            randomButton.onclick = function(e) {
                _this.isRandom = !_this.isRandom
                _this.setConfig('isRandom', _this.isRandom)
                randomButton.classList.toggle('active', _this.isRandom)
            }

            // Repeat
            repeatButton.onclick = function (e) {
                _this.isRepeat = !_this.isRepeat
                _this.setConfig('isRepeat', _this.isRepeat)
                repeatButton.classList.toggle('active', _this.isRepeat)
            }
            
            // Audio ended -> next song
            audio.onended = function () {
                if (_this.isRepeat) {
                    audio.play()
                } else {
                    nextButton.click()
                }
            }

            // Play song when click 
            playlist.onclick = function (e) {
                const songNode = e.target.closest('.song:not(.active)')
                if ((songNode) || e.target.closest('.option')) {
                    // Click song
                    if (songNode) {
                        _this.currentIndex = Number(songNode.dataset.index)
                        _this.loadCurrentSong()
                        _this.render()
                        audio.play()
                    } 
                    // Click Option
                    if (e.target.closest('.option')) {

                    }
                }
            }
        }
    },

    loadCurrentSong: function() {
        heading.textContent = this.currentSong.name;
        cdThumb.style.backgroundImage = `url('${this.currentSong.image}')`
        audio.src = this.currentSong.path
    },

    scrolltoActiveSong: function() {
        setTimeout(() => {
            $('.song.active').scrollIntoView({
                behavior: 'smooth',
                block: 'center'
            }, 300)
        })
    },

    loadConfig: function() {
        this.isRandom = this.config.isRandom
        this.isRepeat = this.config.isRepeat
    },

    nextSong: function() {
        this.currentIndex++
        if (this.currentIndex >= this.songs.length) {
            this.currentIndex = 0
        }
        this.loadCurrentSong()
    },

    prevSong: function() {
        this.currentIndex--
        if (this.currentIndex < 0) {
            this.currentIndex = this.songs.length -1
        }
        this.loadCurrentSong()
    },

    playRandomSong: function() {
        let newIndex 
        do {
            newIndex = Math.floor(Math.random() * this.songs.length)
        } while (newIndex === this.currentIndex)
        
        this.currentIndex = newIndex
        this.loadCurrentSong()
    },

    start: function() {
        // Load Config
        this.loadConfig();

        // Define Object's Atrributes
        this.defineProperties();

        // Listen/Handle Event
        this.handleEvents();

        // Load current song into UI
        this.loadCurrentSong();

        // Render playlists
        this.render();

        // Initial Button random & repeat
        randomButton.classList.toggle('active', this.isRandom)
        repeatButton.classList.toggle('active', this.isRepeat)
    },
}

app.start();

