import React, { useState } from 'react';
import { Languages, Send, Loader2 } from 'lucide-react';

// Type definitions for better type safety
interface FormData {
  time_alone: number;
  stage_fear: number;
  social_events: number;
  going_outside: number;
  post_frequency: number;
  friends_circle: number;
  drained_after_socializing: string;
}

interface Translations {
  en: {
    title: string;
    subtitle: string;
    inputs: {
      time_alone: string;
      stage_fear: string;
      social_events: string;
      going_outside: string;
      post_frequency: string;
      friends_circle: string;
      drained_after_socializing: string;
    };
    placeholders: {
      time_alone: string;
      stage_fear: string;
      social_events: string;
      going_outside: string;
      post_frequency: string;
      friends_circle: string;
    };
    hints: {
      time_alone: string;
      stage_fear: string;
      social_events: string;
      going_outside: string;
      post_frequency: string;
      friends_circle: string;
    };
    options: {
      drained_select: string;
      drained_yes: string;
      drained_no: string;
    };
    submitButton: string;
    languageToggle: string;
    results: {
      title: string;
      extrovert: string;
      introvert: string;
      ambivert: string;
      extrovert_desc: string;
      introvert_desc: string;
      ambivert_desc: string;
    };
    loading: string;
    error: string;
  };
  ko: {
    title: string;
    subtitle: string;
    inputs: {
      time_alone: string;
      stage_fear: string;
      social_events: string;
      going_outside: string;
      post_frequency: string;
      friends_circle: string;
      drained_after_socializing: string;
    };
    placeholders: {
      time_alone: string;
      stage_fear: string;
      social_events: string;
      going_outside: string;
      post_frequency: string;
      friends_circle: string;
    };
    hints: {
      time_alone: string;
      stage_fear: string;
      social_events: string;
      going_outside: string;
      post_frequency: string;
      friends_circle: string;
    };
    options: {
      drained_select: string;
      drained_yes: string;
      drained_no: string;
    };
    submitButton: string;
    languageToggle: string;
    results: {
      title: string;
      extrovert: string;
      introvert: string;
      ambivert: string;
      extrovert_desc: string;
      introvert_desc: string;
      ambivert_desc: string;
    };
    loading: string;
    error: string;
  };
}

// Translation object with English and Korean text - Enhanced with ambivert support
const translations: Translations = {
  en: {
    title: "🧠 Personality Predictor",
    subtitle: "Discover whether you're an Extrovert, Introvert, or Ambivert based on your social patterns",
    inputs: {
      time_alone: "⏰ Time Spent Alone",
      stage_fear: "🎭 Stage Fear Level",
      social_events: "🎉 Social Event Attendance",
      going_outside: "🚶 Going Outside Frequency",
      post_frequency: "📱 Social Media Post Frequency",
      friends_circle: "👥 Friends Circle Size",
      drained_after_socializing: "😴 Drained After Socializing"
    },
    placeholders: {
      time_alone: "8",
      stage_fear: "5",
      social_events: "5",
      going_outside: "5",
      post_frequency: "5",
      friends_circle: "10"
    },
    hints: {
      time_alone: "Hours per day (0-24)",
      stage_fear: "1 = No fear, 10 = Extreme fear",
      social_events: "1 = Rarely attend, 10 = Always attend",
      going_outside: "1 = Rarely go out, 10 = Always outside",
      post_frequency: "Posts per month (0-50)",
      friends_circle: "Number of close friends"
    },
    options: {
      drained_select: "Choose an option...",
      drained_yes: "Yes - I feel drained",
      drained_no: "No - I feel energized"
    },
    submitButton: "🔮 Predict My Personality",
    languageToggle: "한국어",
    results: {
      title: "Your Personality Type:",
      extrovert: "Extrovert 🦁",
      introvert: "Introvert 🦉",
      ambivert: "Ambivert 🐼",
      extrovert_desc: "You tend to gain energy from social interactions and external stimulation. You're outgoing, sociable, and thrive in group settings!",
      introvert_desc: "You tend to gain energy from solitude and internal reflection. You prefer deep, meaningful conversations and smaller social circles!",
      ambivert_desc: "You balance both introverted and extroverted tendencies. You're adaptable and can thrive in various social situations!"
    },
    loading: "Analyzing...",
    error: "Error occurred. Please try again."
  },
  ko: {
    title: "🧠 성격 예측기",
    subtitle: "당신의 사회적 패턴을 바탕으로 외향적, 내향적, 양향적 성격을 알아보세요",
    inputs: {
      time_alone: "⏰ 혼자 보내는 시간",
      stage_fear: "🎭 무대 공포 수준",
      social_events: "🎉 사회적 행사 참석도",
      going_outside: "🚶 외출 빈도",
      post_frequency: "📱 소셜미디어 게시 빈도",
      friends_circle: "👥 친구 관계 규모",
      drained_after_socializing: "😴 사교 후 피로감"
    },
    placeholders: {
      time_alone: "8",
      stage_fear: "5",
      social_events: "5",
      going_outside: "5",
      post_frequency: "5",
      friends_circle: "10"
    },
    hints: {
      time_alone: "하루 시간 (0-24)",
      stage_fear: "1 = 무서움 없음, 10 = 극심한 무서움",
      social_events: "1 = 거의 참석하지 않음, 10 = 항상 참석",
      going_outside: "1 = 거의 외출하지 않음, 10 = 항상 외출",
      post_frequency: "월별 게시물 수 (0-50)",
      friends_circle: "가까운 친구의 수"
    },
    options: {
      drained_select: "옵션을 선택하세요...",
      drained_yes: "예 - 피로감을 느낍니다",
      drained_no: "아니요 - 활력을 느낍니다"
    },
    submitButton: "🔮 내 성격 예측하기",
    languageToggle: "English",
    results: {
      title: "당신의 성격 유형:",
      extrovert: "외향형 🦁",
      introvert: "내향형 🦉",
      ambivert: "양향형 🐼",
      extrovert_desc: "당신은 사회적 상호작용과 외부 자극으로부터 에너지를 얻는 경향이 있습니다. 당신은 외향적이고 사교적이며 그룹 환경에서 번영합니다!",
      introvert_desc: "당신은 고독과 내적 성찰로부터 에너지를 얻는 경향이 있습니다. 당신은 깊고 의미 있는 대화와 더 작은 사회적 관계를 선호합니다!",
      ambivert_desc: "당신은 내향성과 외향성을 모두 균형 있게 가지고 있습니다. 다양한 사회적 상황에 적응력이 뛰어나고 번영할 수 있습니다!"
    },
    loading: "분석 중...",
    error: "오류가 발생했습니다. 다시 시도해주세요."
  }
};

function App() {
  // State management for language, form data, result, and loading
  const [language, setLanguage] = useState<'en' | 'ko'>('en');
  const [formData, setFormData] = useState<FormData>({
    time_alone: 0,
    stage_fear: 0,
    social_events: 0,
    going_outside: 0,
    post_frequency: 0,
    friends_circle: 0,
    drained_after_socializing: ''
  });
  const [result, setResult] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Get current translation based on selected language
  const t = translations[language];

  // Handle language toggle
  const toggleLanguage = () => {
    setLanguage(language === 'en' ? 'ko' : 'en');
  };

  // Handle form input changes
  const handleInputChange = (field: keyof FormData, value: string | number) => {
    setFormData(prev => ({
      ...prev,
      [field]: value
    }));
  };

  // Handle form submission - sends data to AI model backend
  const handleSubmit = async () => {
    
    // Reset previous results and errors
    setError(null);
    setResult(null);
    setLoading(true);

    try {
      // Create URLSearchParams body as per your AI model API
      const body = new URLSearchParams();
      Object.entries(formData).forEach(([key, value]) => {
        if (key === 'drained_after_socializing') {
          // Convert yes/no to 1.0/0.0 for AI model
          const drainedValue = value.toLowerCase() === 'yes' ? '1.0' : '0.0';
          body.append(key, drainedValue);
        } else {
          body.append(key, value.toString());
        }
      });

      // API call to your AI model backend
      const response = await fetch('https://personality-predictor-ezbd.onrender.com', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error(`Server error: ${response.statusText}`);
      }

      const data = await response.json();
      
      // Handle the prediction result from your AI model
      const prediction = data.prediction || data.personality || 'Unknown';
      setResult(prediction);
      
    } catch (err: any) {
      setError(err.message || 'An error occurred while predicting personality');
      console.error('Prediction error:', err);
    } finally {
      setLoading(false);
    }
  };

  // Validate form - check if all required fields are filled
  const isFormValid = () => {
    return (
      formData.time_alone > 0 &&
      formData.stage_fear > 0 &&
      formData.social_events > 0 &&
      formData.going_outside > 0 &&
      formData.post_frequency >= 0 &&
      formData.friends_circle >= 0 &&
      formData.drained_after_socializing !== ''
    );
  };

  // Get result display data based on prediction
  const getResultDisplay = (prediction: string) => {
    const predictionLower = prediction.toLowerCase();
    if (predictionLower.includes('extrovert')) {
      return {
        emoji: '🦁',
        title: t.results.extrovert,
        description: t.results.extrovert_desc,
        colorClass: 'from-orange-100 to-pink-100 border-orange-500'
      };
    } else if (predictionLower.includes('introvert')) {
      return {
        emoji: '🦉',
        title: t.results.introvert,
        description: t.results.introvert_desc,
        colorClass: 'from-blue-100 to-purple-100 border-blue-500'
      };
    } else if (predictionLower.includes('ambivert')) {
      return {
        emoji: '🐼',
        title: t.results.ambivert,
        description: t.results.ambivert_desc,
        colorClass: 'from-green-100 to-emerald-100 border-green-500'
      };
    } else {
      return {
        emoji: '🤔',
        title: prediction,
        description: 'Personality analysis complete.',
        colorClass: 'from-gray-100 to-slate-100 border-gray-500'
      };
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 via-blue-900 to-indigo-900 relative overflow-hidden">
      {/* Animated background particles */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute w-4 h-4 bg-white/10 rounded-full animate-pulse" style={{ top: '10%', left: '10%', animationDelay: '0s' }}></div>
        <div className="absolute w-6 h-6 bg-white/5 rounded-full animate-pulse" style={{ top: '20%', right: '20%', animationDelay: '1s' }}></div>
        <div className="absolute w-3 h-3 bg-white/15 rounded-full animate-pulse" style={{ bottom: '30%', left: '15%', animationDelay: '2s' }}></div>
        <div className="absolute w-5 h-5 bg-white/8 rounded-full animate-pulse" style={{ bottom: '20%', right: '10%', animationDelay: '3s' }}></div>
        <div className="absolute w-4 h-4 bg-white/12 rounded-full animate-pulse" style={{ top: '60%', left: '80%', animationDelay: '4s' }}></div>
        <div className="absolute w-2 h-2 bg-white/20 rounded-full animate-pulse" style={{ top: '40%', right: '60%', animationDelay: '5s' }}></div>
      </div>

      <div className="container mx-auto px-4 py-8 max-w-4xl relative z-10">
        {/* Main card */}
        <div className="bg-white/95 backdrop-blur-sm rounded-2xl shadow-2xl overflow-hidden">
          {/* Header */}
          <div className="bg-gradient-to-r from-purple-600 to-blue-600 text-white p-6 md:p-8">
            <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
              <div className="flex-1">
                <h1 className="text-2xl md:text-3xl font-bold mb-2">{t.title}</h1>
                <p className="text-purple-100 text-sm md:text-base">{t.subtitle}</p>
              </div>
              
              {/* Language toggle */}
              <div className="flex bg-white/20 rounded-lg p-1">
                <button
                  onClick={() => setLanguage('en')}
                  className={`px-3 py-2 rounded-md text-sm font-medium transition-all duration-200 ${
                    language === 'en' 
                      ? 'bg-white text-purple-600 shadow-sm' 
                      : 'text-white hover:bg-white/10'
                  }`}
                >
                  English
                </button>
                <button
                  onClick={() => setLanguage('ko')}
                  className={`px-3 py-2 rounded-md text-sm font-medium transition-all duration-200 ${
                    language === 'ko' 
                      ? 'bg-white text-purple-600 shadow-sm' 
                      : 'text-white hover:bg-white/10'
                  }`}
                >
                  한국어
                </button>
              </div>
            </div>
          </div>

          {/* Form */}
          <div className="p-6 md:p-8">
            <div className="space-y-6">
              {/* Form rows - responsive grid */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {/* Time Alone */}
                <div className="space-y-2">
                  <label htmlFor="time_alone" className="block text-sm font-semibold text-gray-700">
                    {t.inputs.time_alone}
                  </label>
                  <input
                    type="number"
                    id="time_alone"
                    value={formData.time_alone || ''}
                    onChange={(e) => handleInputChange('time_alone', parseFloat(e.target.value) || 0)}
                    placeholder={t.placeholders.time_alone}
                    min="0"
                    max="24"
                    step="0.5"
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-colors duration-200"
                    required
                  />
                  <p className="text-xs text-gray-500">{t.hints.time_alone}</p>
                </div>

                {/* Stage Fear */}
                <div className="space-y-2">
                  <label htmlFor="stage_fear" className="block text-sm font-semibold text-gray-700">
                    {t.inputs.stage_fear}
                  </label>
                  <input
                    type="number"
                    id="stage_fear"
                    value={formData.stage_fear || ''}
                    onChange={(e) => handleInputChange('stage_fear', parseInt(e.target.value) || 0)}
                    placeholder={t.placeholders.stage_fear}
                    min="1"
                    max="10"
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-colors duration-200"
                    required
                  />
                  <p className="text-xs text-gray-500">{t.hints.stage_fear}</p>
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {/* Social Events */}
                <div className="space-y-2">
                  <label htmlFor="social_events" className="block text-sm font-semibold text-gray-700">
                    {t.inputs.social_events}
                  </label>
                  <input
                    type="number"
                    id="social_events"
                    value={formData.social_events || ''}
                    onChange={(e) => handleInputChange('social_events', parseInt(e.target.value) || 0)}
                    placeholder={t.placeholders.social_events}
                    min="0"
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-colors duration-200"
                    required
                  />
                  <p className="text-xs text-gray-500">{t.hints.social_events}</p>
                </div>

                {/* Going Outside */}
                <div className="space-y-2">
                  <label htmlFor="going_outside" className="block text-sm font-semibold text-gray-700">
                    {t.inputs.going_outside}
                  </label>
                  <input
                    type="number"
                    id="going_outside"
                    value={formData.going_outside || ''}
                    onChange={(e) => handleInputChange('going_outside', parseInt(e.target.value) || 0)}
                    placeholder={t.placeholders.going_outside}
                    min="1"
                    max="10"
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-colors duration-200"
                    required
                  />
                  <p className="text-xs text-gray-500">{t.hints.going_outside}</p>
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {/* Post Frequency */}
                <div className="space-y-2">
                  <label htmlFor="post_frequency" className="block text-sm font-semibold text-gray-700">
                    {t.inputs.post_frequency}
                  </label>
                  <input
                    type="number"
                    id="post_frequency"
                    value={formData.post_frequency || ''}
                    onChange={(e) => handleInputChange('post_frequency', parseInt(e.target.value) || 0)}
                    placeholder={t.placeholders.post_frequency}
                    min="0"
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-colors duration-200"
                    required
                  />
                  <p className="text-xs text-gray-500">{t.hints.post_frequency}</p>
                </div>

                {/* Friends Circle */}
                <div className="space-y-2">
                  <label htmlFor="friends_circle" className="block text-sm font-semibold text-gray-700">
                    {t.inputs.friends_circle}
                  </label>
                  <input
                    type="number"
                    id="friends_circle"
                    value={formData.friends_circle || ''}
                    onChange={(e) => handleInputChange('friends_circle', parseInt(e.target.value) || 0)}
                    placeholder={t.placeholders.friends_circle}
                    min="0"
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-colors duration-200"
                    required
                  />
                  <p className="text-xs text-gray-500">{t.hints.friends_circle}</p>
                </div>
              </div>

              {/* Drained After Socializing - Full width */}
              <div className="space-y-2">
                <label htmlFor="drained_after_socializing" className="block text-sm font-semibold text-gray-700">
                  {t.inputs.drained_after_socializing}
                </label>
                <select
                  id="drained_after_socializing"
                  value={formData.drained_after_socializing}
                  onChange={(e) => handleInputChange('drained_after_socializing', e.target.value)}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-colors duration-200"
                  required
                >
                  <option value="" disabled>{t.options.drained_select}</option>
                  <option value="yes">{t.options.drained_yes}</option>
                  <option value="no">{t.options.drained_no}</option>
                </select>
              </div>

              {/* Submit button */}
              <button
                onClick={handleSubmit}
                disabled={!isFormValid() || loading}
                className="w-full bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-700 hover:to-blue-700 disabled:from-gray-400 disabled:to-gray-500 disabled:cursor-not-allowed text-white font-semibold py-4 px-6 rounded-lg transition-all duration-200 flex items-center justify-center space-x-2 shadow-lg hover:shadow-xl transform hover:-translate-y-0.5"
              >
                {loading ? (
                  <>
                    <Loader2 className="h-5 w-5 animate-spin" />
                    <span>{t.loading}</span>
                  </>
                ) : (
                  <span>{t.submitButton}</span>
                )}
              </button>
            </div>
          </div>

          {/* Result display */}
          {result && (
            <div className="mx-6 md:mx-8 mb-6 md:mb-8">
              {(() => {
                const resultDisplay = getResultDisplay(result);
                return (
                  <div className={`rounded-xl p-6 text-center shadow-lg bg-gradient-to-r ${resultDisplay.colorClass} border-l-4`}>
                    <div className="text-4xl mb-3">
                      {resultDisplay.emoji}
                    </div>
                    <h3 className="text-xl font-bold text-gray-800 mb-2">{t.results.title}</h3>
                    <div className="text-2xl font-bold mb-4 text-gray-900">
                      {resultDisplay.title}
                    </div>
                    <p className="text-gray-700 leading-relaxed">
                      {resultDisplay.description}
                    </p>
                  </div>
                );
              })()}
            </div>
          )}

          {/* Error display */}
          {error && (
            <div className="mx-6 md:mx-8 mb-6 md:mb-8">
              <div className="bg-red-50 border border-red-200 rounded-xl p-4">
                <p className="text-red-800 font-medium">{error}</p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
