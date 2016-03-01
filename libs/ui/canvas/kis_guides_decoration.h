/*
 *  Copyright (c) 2016 Dmitry Kazakov <dimula73@gmail.com>
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program; if not, write to the Free Software
 *  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 */

#ifndef __KIS_GUIDES_DECORATION_H
#define __KIS_GUIDES_DECORATION_H

#include <QScopedPointer>
#include "kis_canvas_decoration.h"

class KoGuidesData;

static const QString GUIDES_DECORATION_ID = "guides-decoration";

class KRITAUI_EXPORT KisGuidesDecoration : public KisCanvasDecoration
{
    Q_OBJECT
public:
    KisGuidesDecoration(QPointer<KisView> view);
    ~KisGuidesDecoration();


    void setGuidesData(const KoGuidesData &value);
    const KoGuidesData& guidesData() const;

protected:
    void drawDecoration(QPainter& gc, const QRectF& updateArea, const KisCoordinatesConverter *converter, KisCanvas2 *canvas);

private:
    struct Private;
    const QScopedPointer<Private> m_d;
};

#endif /* __KIS_GUIDES_DECORATION_H */