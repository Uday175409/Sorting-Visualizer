import React from 'react';

const Controls = ({
    algorithm,
    setAlgorithm,
    arraySize,
    setArraySize,
    speed,
    setSpeed,
    onGenerate,
    onSort,
    onReset,
    isSorting
}) => {
    return (
        <div className="bg-white p-6 rounded-lg shadow-md mb-6 transition-all duration-300 hover:shadow-lg">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 items-end">
                {/* Algorithm Selection */}
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">Algorithm</label>
                    <select
                        value={algorithm}
                        onChange={(e) => setAlgorithm(e.target.value)}
                        disabled={isSorting}
                        className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors disabled:opacity-50"
                    >
                        <option value="bubble">Bubble Sort</option>
                        <option value="selection">Selection Sort</option>
                        <option value="insertion">Insertion Sort</option>
                        <option value="merge">Merge Sort</option>
                        <option value="quick">Quick Sort</option>
                        <option value="heap">Heap Sort</option>
                    </select>
                </div>

                {/* Array Size */}
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                        Array Size: {arraySize}
                    </label>
                    <input
                        type="range"
                        min="5"
                        max="100"
                        value={arraySize}
                        onChange={(e) => setArraySize(Number(e.target.value))}
                        disabled={isSorting}
                        className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer disabled:opacity-50 accent-blue-600"
                    />
                </div>

                {/* Speed Control */}
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                        Speed: {speed}ms
                    </label>
                    <select
                        value={speed}
                        onChange={(e) => setSpeed(Number(e.target.value))}
                        disabled={isSorting}
                        className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 disabled:opacity-50"
                    >
                        <option value={500}>Slow (500ms)</option>
                        <option value={200}>Medium (200ms)</option>
                        <option value={50}>Fast (50ms)</option>
                        <option value={10}>Ultra Fast (10ms)</option>
                    </select>
                </div>

                {/* Actions */}
                <div className="flex space-x-2">
                    <button
                        onClick={onGenerate}
                        disabled={isSorting}
                        className="flex-1 px-4 py-2 bg-gray-600 text-white rounded-md hover:bg-gray-700 transition-colors disabled:opacity-50"
                    >
                        New Array
                    </button>
                    <button
                        onClick={onSort}
                        disabled={isSorting}
                        className="flex-1 px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors disabled:opacity-50 font-semibold"
                    >
                        {isSorting ? 'Sorting...' : 'Sort'}
                    </button>
                    <button
                        onClick={onReset}
                        className="px-4 py-2 bg-red-500 text-white rounded-md hover:bg-red-600 transition-colors disabled:opacity-50"
                    >
                        Reset
                    </button>
                </div>
            </div>
        </div>
    );
};

export default Controls;
